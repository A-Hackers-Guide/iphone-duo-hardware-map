# `/System/DriverKit/usr/lib/system/libcorecrypto.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,044,208 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 2744)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/System/DriverKit/usr/lib/system/libcorecrypto.dylib (compatibility version 1.0.0, current version 2109.40.22)`
- `/System/DriverKit/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/System/DriverKit/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/System/DriverKit/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/System/DriverKit/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/System/DriverKit/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/System/DriverKit/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/System/DriverKit/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/System/DriverKit/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/System/DriverKit/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`

## Entitlements

```xml
  - no entitlements
```

## Strings (533)

```
fipspost_post_hmac
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_consistency\n
fipspost_post_integrity
cccast_cbc_decrypt_mode
cckem_generate_key_with_seed
fipspost_post_aes_cbc
pubkey:
fipspost_post_ecdsa_verify_ws
%02X
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: Unexpected SUCCESS\n
ccrng_process_init
FIPSPOST_USER [%llu] %s:%d: MAC generated: 
fipspost_post_ecdsa_kat_sign_ws
\xbe\xe1\x92\xef&ݻ#j\xf8)\xd0\xc7\xd8I\xb7
fipspost_post_mlkem_encapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sk: %d\n
dq = 0x
qinv=0x
fipspost_post_mlkem_keygen
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch pubkey: %d\n
fipspost_post_mlkem_pairwise
AES_XTS_INTEL_AESNI
cccast_ecb_decrypt_mode
%s { x -> 
fipspost_post_aes_ecb_decrypt
Software
ccdh_import_priv
ccrsa_encrypt_oaep
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n
fipspost_post_mldsa_sign_rejection_kat_44
SHA512_VNG_ARM_HW
ccdh_gp_rfc3526group17
cchpke_kem_generate_key_pair
ccsigma_seal
ccmldsa_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_full\n
cccmac_one_shot_generate
cchpke_responder_decrypt
getentropy
SHA1_VNG_INTEL_AVX2
ccdes3_ecb_encrypt_mode
ccdh_gp_rfc2409group02
ccspake_kex_generate
wrap-sha512-kek-aes128
FIPSPOST_USER [%llu] %s:%d: FAILED: decrypt\n
Attempt to access y value of share out of share bag with invalid share index
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_kat\n
ccpad_cts2_decrypt
ccblowfish_ecb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv (P-%zu/SHA-%zu): %d\n
SHA512_VNG_INTEL_AVX1
ccdes3_ctr_crypt_mode
ccdh_gp_rfc5114_MODP_1024_160
public key 
UNKNOWN
ccdrbg_done
ccdes3_cfb8_encrypt_mode
free ws
p  = 0x
q  = 0x
SHA1_VNG_INTEL_AVX1
ccpad_cts1_encrypt
ccsha256_di
ccrsa_verify_pkcs1v15_msg
ccmd2_di
ccspake_mac_hkdf_derive
ccmldsa_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_sign_pkcs1v15\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
16
ccrsa_sign_pkcs1v15_msg
cchpke
ccspake_mac_hkdf_hmac_compute
cckem_mlkem1024
fipspost_post_mlkem
fipspost_post_ecdh_ws
fipspost_post_pbkdf
ccmldsa87
M\xac%]
ccrsa_generate_fips186_key
ccec_rfc6637_kdf
ccrc2_cfb8_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (s)\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot decrypt\n
cced25519_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 1600-bit message failed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: rc: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch ek: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-256): %d\n
cccast_cfb_decrypt_mode
ccmldsa_verify_with_context
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_pub (P-%zu/SHA-%zu): %d\n
wrap-sha256-kex-aes128wrap
ccdrbg_generate
cchkdf
fipspost_post_mldsa
SAE Hunting and Pecking
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-512): %d\n
27.0
ccrsa_verify_pss_msg
fipspost_post_rsa_sig
Failed to generate a valid signature
FIPSPOST_USER [%llu] %s:%d:   In variable: 
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n
ccsae_init_p256_sha256
ccaes_gcm_decrypt_mode
SHA3_VNG_ARM_HW
ccecdh_generate_key
P256-SHA256-SSWU-RO-
SHA3_VNG_ARM
ccec_cp_384
fipspost_post_mldsa_keygen
AES_XTS_GENERIC
SHA384_VNG_ARM_HW
ccrng_process_atfork_child
ccaes_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt one_shot\n
AES_XTS_INTEL_OPT
FIPSPOST_USER [%llu] %s:%d: FAILED: len(plaintext) != len(message)\n
ccdh_gp_rfc3526group18
6144
ccdh_compute_shared_secret
ccblowfish_cfb_encrypt_mode
fipspost_post_aes_gcm
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n
ccsha1_di
ccrsa_decrypt_oaep
ccblowfish_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: memcmp\n
fipspost_post_drbg_ctr
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sig: %d\n
ccsrp_gp_rfc5054_2048
ccss_shamir_poly_coefficient with index bigger than or equal to threshold
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n
\x9b\xc2\v)Q\xffr\xd3\xf2\x80\xff;\xd2\xdc=\xcc
SHA512_VNG_INTEL_AVX2
Z\xc9\xf7\xec8\xf6\x8bv#\x94\xd3\xca\xec륻
ccpad_cts1_decrypt
ccec_sign_msg
ccrsa_sign_pkcs1v15
priv: {
ccdh_gp_rfc3526group14
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_VER KAT #%zu\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES128): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 0-bit message failed\n
ep r traffic
AES_XTS_ARM_ALIGNED
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_512 KAT\n
ccaes_cfb_decrypt_mode
cckem_encapsulate
ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n
42
ccdrbg_reseed
ccblowfish_ecb_encrypt_mode
ccblowfish_cfb_decrypt_mode
ccrsa_generate_fips186_key consistency
ccec_sign
corecrypto process rng
SHA1_VNG_INTEL_SUPPLEMENTAL_SSE3
cccmac_one_shot_verify
ccec_validate_pub
fipspost_post_rsa_enc_dec
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_extract_rs (P-%zu/SHA-%zu): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-512): %d\n
8192
ccec_cp_521
fipspost_post_rsa_oaep_kat_ws
fipspost_post_rsa_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #2: %d\n
ccec_make_pub
NULL
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA256 KAT\n
ccaes_gcm_encrypt_mode
fipspost_post_aes_xts
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES256 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA512 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n
SHA256_ARMV6M
ccsha3_512_di
ccshake128_xi
ccdes3_ecb_decrypt_mode
ccdh_gp_rfc5114_MODP_2048_256
ccmldsa65
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #32: %d\n
ccsha224_di
ccblowfish_ctr_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n
Apple corecrypto Module
ccrc2_cfb_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate\n
ccaes_ccm_decrypt_mode
3072
ccrc2_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA2 KAT\n
AES_ECB_INTEL_OPT
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #47: %d\n
ccaes_cfb8_encrypt_mode
ccsha384_di
ccec_cp_224
SHA256_VNG_INTEL_AVX1
ccrng_process_atfork_prepare
AES_XTS_ARM
fipspost_post_ecdh
fipspost_post_kdf_ctr
full key %s { \n
not implemented
secret-key
sha512/256
FIPSPOST_USER [%llu] %s:%d: FAILED: result: %d\n
ccdh_gp_rfc3526group15
24
fipspost_post_ffdh
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_verify_msg (P-%zu/SHA-%zu): %d\n
\xfa\f\xce\xd2.\x89k@
AES_ECB_ARM_ALIGNED
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
fipspost_post_ecdsa_pairwise_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate 2\n
%zu bit rsa key\n
ccdh_import_pub
ccaes_cfb8_decrypt_mode
ccec_rfc6637_wrap_key
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt authentication\n
fipspost_post_aes_ecb
fipspost_post_hkdf
value to digest
PpKpAmtfcDCPtAtwRMnHBueaQklIgpzLiH
ccrsa_verify_pkcs1v15_digest
FIPSPOST_USER [%llu] %s:%d: FAILED: sig != expected signature\n
, z -> 
P384-SHA512-SSWU-RO-
FIPSPOST_USER [%llu] %s:%d: FAILED: test %d\n
SHA256_VNG_INTEL_AVX2
fipspost_post_rsa_oaep_consistency_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #89: %d\n
ccpad_cts3_decrypt
ccsha3_384_di
ccspake_kex_process
fipspost_post_ecdsa_kat_verify_ws
ccrng
fipspost_run_post
FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - %s\n
ccaes_ctr_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_init\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_224 KAT\n
%s v%s [%s, %s, %s, %s, %s]
32
1024
Anonymous Sender    
sha3_384
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-512): %d\n
ccdes3_cfb_decrypt_mode
fipspost_post_ecdsa_sign_ws
cchmac
cccast_ctr_crypt_mode
ccspake_mac_hkdf_hmac_sha512
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n
SHA256_VNG_INTEL_SUPPLEMENTAL_SSE3
FIPSPOST_USER [%llu] %s:%d: FAILED: failed AES-CMAC KAT\n
ccnistkdf_ctr_hmac
cced25519_make_key_pair
FIPSPOST_USER [%llu] %s:%d: FAILED: digest: %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: could not create the hash\n
alloc ws
ccdes3_cbc_decrypt_mode
ccdes3_ofb_crypt_mode
ccrc4
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
sha256
Failed to pick a random Miller-Rabin base
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA1 KAT\n
ccecies_encrypt_gcm
cchpke_initiator_encrypt
ccsae_init
ccmldsa_sign_prehashed
fipspost_post_aes_cmac
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt cmp\n
FIPSPOST_USER [%llu] %s:%d: FAILED: %s: %d\n
m  = 0x
AES_ECB_LTC
ccpad_cts3_encrypt
ccaes_ecb_encrypt_mode
2048
ccblowfish_cbc_decrypt_mode
fipspost_post_mldsa_pairwise
SHA256_VNG_ARM
AES_ECB_TRNG
ccansikdf_x963
ccdh_gp_apple768
ccsigma_sign
ccdes_ecb_encrypt_mode
fipspost_post_aes_ccm
SHA512_VNG_INTEL_SUPPLEMENTAL_SSE3
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_encrypt_oaep\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-256): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n
SHA512_LTC
ccec_cp_192
ccdes3_cfb8_decrypt_mode
ccrmd160_di
fipspost_post_kdf_ctr_cmac
__text
SHA1_VNG_ARM
ccec_generate_key_fips
fipspost_post_rsa_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-384): %d\n
ccaes_ccm_encrypt_mode
cccast_cfb8_encrypt_mode
:
SHA3_VNG_INTEL
ccmldsa_generate_key_with_seed
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_SIG KAT #%zu\n
ccec_generate_key_fips consistency
FIPSPOST_USER [%llu] %s:%d: FAILED: encrypt\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #0: %d\n
cccast_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: expected SUCCESS\n
fipspost_post_aes_ecb_encrypt
ccrng failed assert cbc_info->block_size = %lu\n
4096
cccast_ecb_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-224): %d\n
Apple ARM
ccdes3_cbc_encrypt_mode
fipspost_post
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n
AES_ECB_ARM
\xf2f\xa1\x87
ccrc2_cfb8_encrypt_mode
ccss_shamir_share_generator_generate_share
cckem_decapsulate
SHA384_VNG_INTEL_AVX2
User
ccecies_decrypt_gcm
ccrc2_ecb_decrypt_mode
fipspost_post_mldsa_verify_kat
ccsha3_224_di
fipspost_post_ffdh_pairwise_ws
Failed to generate random
ccwrap_auth_decrypt_withiv
ccshake256_xi
sha3_256
fipspost_post_mlkem_decapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA512 KAT\n
ccmd5_di
ccec_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_224 KAT\n
ccrc2_ctr_crypt_mode
cckem_mlkem768
fipspost_post_mldsa_sign_kat
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_384 KAT\n
ccdh_generate_key
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_compute_shared_secret\n
fipspost_post_indicator
SeiPcvDyiAvRsPPKX
SAE KCK and PMK
ccrc2_ecb_encrypt_mode
ccsae_get_keys
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n
sha3_512
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: AES-CBC KAT Failed %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-512): %d\n
ccdrbg_nistctr: invalid block size
ccec_rfc6637_unwrap_key
ccrc2_cbc_decrypt_mode
ccsha512_256_di
ccpad_cts2_encrypt
FIPSPOST_USER [%llu] %s:%d: [FIPSPOST][Module-ID] %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_sign_msg (P-%zu/SHA-%zu): %d\n
SHA384_LTC
ccec_cp_256
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 0-bit message failed\n
P521-SHA512-SSWU-RO-
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n
ccblowfish_cbc_encrypt_mode
cchpke_kem_x25519_generate_key_pair
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-1): %d\n
cced25519_verify
cchpke_export_secret
ccsigma_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n
Attempt to copy x value of share out of share bag with invalid share index
ccaes_xts_decrypt_mode
ccnistkdf_ctr_cmac_fixed
cckem_generate_key
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-384): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n
AES_ECB_INTEL_AESNI
ccspake_mac_hkdf_cmac_aes128_sha256
fipspost_post_shake
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #79: %d\n
ccdrbg_factory_nistctr
ccrsa_sign_pss_msg
ccblowfish_cfb8_decrypt_mode
ccec_verify_strict
ccrc2_cfb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt authentication\n
, y -> 
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-256): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv\n
dp = 0x
ʃ\xd6E^\x98\xcd\t\xd6e\x86\xe2c\x92m\xe6
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n
SHA384_VNG_INTEL_SUPPLEMENTAL_SSE3
fipspost_post_rsa_oaep_decrypt_ws
INVALID Module ID
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES256): %d\n
ccdrbg_nistctr: key length too long
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt cmp\n
SHA384_VNG_INTEL_AVX1
ccaes_cfb_encrypt_mode
ccsha3_256_di
ccnistkdf_ctr_cmac
cccast_cfb_encrypt_mode
fipspost_post_drbg_hmac
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-256): %d\n
ccdrbg_factory_nisthmac
fipspost_post_rsa_pairwise
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n
h\x8b\x9e(#+vT\xf95\x93\xa5\xc3\xf085
ccaes_ecb_decrypt_mode
ccrc2_cbc_encrypt_mode
ccmldsa_verify_prehashed
sha1
SHA256_LTC
SHA1_LTC
%s
ccpbkdf2_hmac
SHA256_VNG_ARM64_NEON
FIPSPOST_USER [%llu] %s:%d: FAILED: plaintext != message\n
}\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_import_priv\n
ccnistkdf_ctr_hmac_fixed
%.016llx
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n
ccaes_cbc_encrypt_mode
fipspost_get_hmac
roAhfqRBzTqHATLXmmLLiQIyBUchpmcqrXWMWoztGqWZrEbqIZFKWphBFbGkoJmnRaqDXZaYMreSUJhWTLypGstb
ccrng_generate
ccdes3_cfb_encrypt_mode
AES_ECB_SKG
ccaes_cbc_decrypt_mode
ccrsa_sign_pss
ccss_shamir_parameters_init
ccmldsa_generate_key
d  = 0x
CCAES_KEY_SIZE_128
CCAES_KEY_SIZE_256
ccspake_cp_256
sha512
__TEXT
ccblowfish_cfb8_encrypt_mode
sha3_224
__TEXT_EXEC
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot encrypt\n
ccdit_managed_context_begin MUST have been called
ccrng_uniform
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (r)\n
ccsae_ctr_hmac_fixed
ep i traffic
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-1): %d\n
ccrng failed assert key_nbytes = %lu\n
SHA3_C
ccdh_gp_rfc3526group16
fipspost_post_ecdsa
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES128 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 1600-bit message failed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed 2\n
ccdh_gp_rfc2409group05
ccrsa_verify_pss_digest
ccss_shamir_share_generator_init
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_verify_pkcs1v15\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt decryption\n
FIPSPOST_USER [%llu] %s:%d: all tests PASSED (%u ms)\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA1 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n
ccaes_xts_encrypt_mode
ccrng_process_atfork_parent
%s { %zu, 
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n
ccdh_gp_rfc5114_MODP_2048_224
SHA512_VNG_ARM
e  = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-224): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_256 KAT\n
ccdrbg_init
ccecdh_compute_shared_secret
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_256 KAT\n
fipspost_post_mldsa_sign_rejection_kat
ccscrypt
ccsigma_init
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_decrypt_oaep\n
ccmd4_di
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt one_shot\n
ccspake_mac_hkdf_hmac_sha256
cccast_cbc_encrypt_mode
ccsha512_di
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_df_bc_init\n
FIPSPOST_USER [%llu] %s:%d: FAILED: HKDF with digest %s\n
ccwrap_auth_encrypt_withiv
ccmldsa_sign_with_context
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt encryption\n
ccrsa_eme_pkcs1v15_decode_generate_random
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_384 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_512 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch privkey: %d\n
SHA256_VNG_ARM_ALIGNED
ccec_make_priv
cccast_cfb8_decrypt_mode
ccec_verify_msg
cch2c
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_pub\n
SHA384_VNG_ARM
ccspake_cp_521
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n
fipspost_post_ffdh_ws
ccspake_cp_384
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: expected SUCCESS\n
```
