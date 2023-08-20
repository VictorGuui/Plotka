from Utils.OpenAI import OpenAI
import pandas as pd
import json


class Message_handler:
    def __init__(self) -> None:
        self.system = "você é um bot que esta ajudando uma pessoa a achar o curso ideal"
        self.AI = OpenAI()
        pass

    def send_message(self, message_history):
        ai_message = self.AI.chat_request(
            message_history=message_history, system=self.system
        )

        #verificar se a mensagem pode gerar um json com o curso
        pass_state = self.verify_information(
            message=ai_message
        )

        if pass_state is not None:
            course_link = self.get_course_link(course_json=pass_state)
            return course_link

        # manter no mesmo e retornar a mensagem
        else:
            return ai_message

        # se retrieve information voltar false, eu mando para o gpt continuar a conversa deste estagio

    def verify_information(self, message):
        json_response = json.loads(
            self.AI.completion(
                prompt="leia a mensagem:\n"
                + message
                + "e retorne uma JSON com o seguinte modelo: { 'curso' : 'curso recomendado', 'motivo' : 'motivo de ter escolhido este curso' }"
            ).replace("'", '"')
        )

        if "curso" in json_response.keys() and "motivo" in json_response.keys():
            if json_response["curso"] != None and json_response["motivo"] != None:
                return json_response

        return None

    def get_course_link(self, course_json):
        course_df = pd.read_csv("assets/cursos.csv", sep=";")
        filtered_df = course_df[
            course_df["nome"].str.contains(course_json["curso"], case=False)
        ]
        course_link = (
            self.AI.completion(
                prompt=f"leia este dataframe {filtered_df[['nome','link']]} e retorne somente o link da linha que mais se assemelha a {course_json['curso']}"
            )
            .replace("\n", "")
            .strip()
        )
        return course_link