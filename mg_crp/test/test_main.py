from mg_crp import CryptoAes, SecretDataAes


def test_main():
    A = CryptoAes(key="Sixteen byte kys")
    secret_data: SecretDataAes = A.encodeAES("Мои секретные данные")
    ###################
    B = CryptoAes(key="Sixteen byte kys")
    assert B.decodeAES(secret_data) == "Мои секретные данные"
