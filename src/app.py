from io import BytesIO

from flask import Flask, send_file
from flask_restful import Resource, Api

from docx_generator.generator_better import generate_learning_goals
from src.resources.generator import Generator

app = Flask(__name__)
api = Api(app)

api.add_resource(Generator, '/generate')


@app.route('/generate_v2', methods=['GET'])
def generate_learning_goal():
    generated_doc = generate_learning_goals('docx_generator/learning_agreement.docx')
    f = BytesIO()
    generated_doc.save(f)
    f.seek(0)
    return send_file(
        f,
        as_attachment=True,
        download_name='generated_learning_goals.docx'
    )


if __name__ == '__main__':
    app.run(debug=True)
