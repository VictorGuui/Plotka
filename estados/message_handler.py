from Utils.OpenAI import OpenAI
import pandas as pd
import json
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

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
            message= ai_message
        )

        if pass_state is not None:
            course_link = self.get_course_link(course_json=pass_state)
            return course_link

        # manter no mesmo e retornar a mensagem
        else:

            return ai_message

        # se retrieve information voltar false, eu mando para o gpt continuar a conversa deste estagio

    def verify_information(self, message):

        match = re.search(r'\{.*?\}', self.AI.completion(
                prompt="leia a mensagem:\n"
                + message
                + " e retorne um JSON com o seguinte modelo: { 'curso' : 'curso recomendado, se ele não recomendou nada, apenas deixe vazio'}"
            ).replace("'", '"'))

        if match:
            json_response = json.loads(match[0])

            if "curso" in json_response.keys():
                if json_response["curso"] != '':
                    return json_response

        return None

    def get_course_link(self, course_json):
        course_df = pd.read_csv("assets/cursos.csv", sep=";")

        most_similar = process.extractOne(course_json["curso"], course_df['nome'])[0]


        link = course_df.loc[course_df['nome'] ==most_similar]['link'].head(1)._values[0]

        link_matches = re.findall(r'https://\S+', link)

        return link_matches[0]