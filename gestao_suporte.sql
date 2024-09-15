CREATE DATABASE gestao_suporte;

USE gestao_suporte;

CREATE TABLE chamados_suporte (
    nome_cliente VARCHAR(100),
    descricao_problema TEXT,
    data_abertura DATE,
    status ENUM('aberto', 'em andamento', 'resolvido'),
    PRIMARY KEY (nome_cliente, data_abertura)
);

SELECT * FROM chamados_suporte;
