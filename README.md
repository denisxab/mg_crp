```python
from mg_crp.crypto_aes import CryptoAes, SecretDataAes

A = CryptoAes(key="Sixteen byte kys")
secret_data: SecretDataAes = A.encodeAES("Мои секретные данные")
###################
B = CryptoAes(key="Sixteen byte kys")
print(B.decodeAES(secret_data))
# Мои секретные данные
```