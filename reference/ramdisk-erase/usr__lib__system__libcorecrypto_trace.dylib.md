# `/usr/lib/system/libcorecrypto_trace.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,046,928 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 2664)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/system/libcorecrypto_trace.dylib (compatibility version 1.0.0, current version 2109.40.22)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_trace.dylib (compatibility version 1.0.0, current version 1966.40.15)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`

## Entitlements

```xml
  - no entitlements
```

## Strings (561)

```
ccblowfish_cfb_encrypt_mode
ccec_rfc6637_wrap_key
fipspost_trace_start
ccaes_cfb_encrypt_mode
NULL
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (r)\n
ccrsa_eme_pkcs1v15_decode_generate_random
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt decryption\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-224): %d\n
SHA384_VNG_INTEL_AVX2
SHA512_VNG_INTEL_AVX1
ccblowfish_cfb8_encrypt_mode
ccsrp_gp_rfc5054_2048
fipspost_post_aes_ecb
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (s)\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA512 KAT\n
cccast_ctr_crypt_mode
ccrc2_ecb_encrypt_mode
com.apple.corecrypto
AES_XTS_INTEL_OPT
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-512): %d\n
ccec_cp_384
ccblowfish_cfb_decrypt_mode
ccaes_cfb8_decrypt_mode
cchpke_initiator_encrypt
SHA512_VNG_ARM_HW
ccss_shamir_share_generator_generate_share
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_verify_msg (P-%zu/SHA-%zu): %d\n
__TEXT_EXEC
FIPSPOST_USER [%llu] %s:%d: TRACE: fips_mode: %x\n
SHA1_VNG_INTEL_SUPPLEMENTAL_SSE3
ccgcm_one_shot
16
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_verify_pkcs1v15\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-256): %d\n
ccrng_generate
cchpke_kem_x25519_generate_key_pair
ep r traffic
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n
SHA384_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-224): %d\n
ccdes3_ecb_encrypt_mode
ccdes3_cfb_decrypt_mode
ccmldsa_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n
AES_XTS_ARM_ALIGNED
ccdh_gp_rfc2409group05
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_extract_rs (P-%zu/SHA-%zu): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_decrypt_oaep\n
ccaes_gcm_encrypt_mode
2048
ccecies_decrypt_gcm
ccsae_get_keys
fipspost_post_ecdsa_kat_sign_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate 2\n
FIPSPOST_USER [%llu] %s:%d: FAILED: test %d\n
fipspost_post_ecdh_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-512): %d\n
Apple corecrypto Module
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: expected SUCCESS\n
e  = 0x
SHA256_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_import_priv\n
Apple ARM
ccmldsa_verify_prehashed
SHA3_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #47: %d\n
6144
fipspost_post_pbkdf
sha512
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_kat\n
ccsha3_256_di
ccdh_gp_rfc3526group15
ccmldsa_sign_prehashed
SHA256_VNG_ARM64_NEON
cccast_cfb_decrypt_mode
cccast_cfb8_encrypt_mode
ccrc2_ecb_decrypt_mode
fipspost_post
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES128): %d\n
alloc ws
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-1): %d\n
FIPSPOST_USER [%llu] %s:%d: TRACE: magic: %x\n
ccdes3_cfb8_encrypt_mode
ccrc2_cbc_decrypt_mode
}\n
fipspost_post_mlkem
ccss_shamir_poly_coefficient with index bigger than or equal to threshold
AES_ECB_LTC
SHA512_LTC
ccrng failed assert key_nbytes = %lu\n
ccdh_gp_rfc2409group02
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-1): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: Unexpected SUCCESS\n
, y -> 
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n
SHA256_VNG_ARM_ALIGNED
AES_ECB_ARM
INVALID Module ID
cccmac_one_shot_verify
fipspost_post_aes_cbc
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 0-bit message failed\n
P521-SHA512-SSWU-RO-
-
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n
ccblowfish_ecb_decrypt_mode
ccdh_gp_rfc5114_MODP_1024_160
ccsae_ctr_hmac_fixed
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt authentication\n
fipspost_post_kdf_ctr_cmac
ccec_generate_key_fips consistency
sha1
m  = 0x
ccaes_xts_decrypt_mode
ccdes3_cbc_encrypt_mode
cckem_mlkem768
FIPSPOST_USER [%llu] %s:%d: FAILED: %s: %d\n
Failed to pick a random Miller-Rabin base
AES_ECB_SKG
%s v%s [%s, %s, %s, %s, %s]
ccblowfish_ctr_crypt_mode
cch2c
fipspost_post_hmac
fipspost_post_mldsa_pairwise
ccsha1_di
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed\n
ccmldsa_sign
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_VER KAT #%zu\n
cchpke_responder_decrypt
fipspost_post_rsa_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_compute_shared_secret\n
ccpad_cts1_decrypt
ccsha512_256_di
ccdes3_ctr_crypt_mode
ccec_cp_521
ccmldsa_generate_key
ccrng_process_atfork_prepare
fipspost_post_mldsa_keygen
ccnistkdf_ctr_hmac
ccshake128_xi
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 0-bit message failed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch privkey: %d\n
SHA256_ARMV6M
ccsha384_di
ccdh_gp_rfc3526group14
32
fipspost_post_rsa_pairwise
FIPSPOST_USER [%llu] %s:%d: FAILED: encrypt\n
ccpad_cts3_encrypt
Anonymous Sender    
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #2: %d\n
ccwrap_auth_encrypt_withiv
ccpad_cts1_encrypt
Failed to generate random
fipspost_post_aes_gcm
ccrng_uniform
cccast_cbc_decrypt_mode
cchmac_internal
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-512): %d\n
fipspost_post_integrity
ccspake_mac_hkdf_hmac_sha512
M\xac%]
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n
fipspost_post_mlkem_decapsulate
ccaes_cbc_encrypt_mode
ccecdh_compute_shared_secret
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n
SHA3_C
27.0
ccrsa_encrypt_oaep
ccblowfish_ofb_crypt_mode
ccec_rfc6637_unwrap_key
ccrng_process_atfork_child
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt one_shot\n
%s { x -> 
P256-SHA256-SSWU-RO-
FIPSPOST_USER [%llu] %s:%d: TRACE: version: %x\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n
AES_ECB_TRNG
SHA1_VNG_INTEL_AVX2
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_256 KAT\n
secret-key
FIPSPOST_USER [%llu] %s:%d: FAILED: result: %d\n
ccaes_xts_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate\n
cccbc_one_shot_explicit_internal
ccmode_gcm_decrypt
fipspost_post_aes_ecb_encrypt
SHA1_LTC
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_consistency\n
cchmac
4096
ccspake_mac_hkdf_hmac_sha256
wrap-sha256-kex-aes128wrap
public key 
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-256): %d\n
SHA256_LTC
SAE KCK and PMK
cccmac_one_shot_generate
cccast_cfb_encrypt_mode
pubkey:
ccdh_gp_rfc3526group16
ccdrbg_reseed
ccspake_mac_hkdf_cmac_aes128_sha256
ccspake_cp_256
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_256 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n
fipspost_post_rsa_oaep_consistency_ws
ccaes_ecb_decrypt_mode
cccast_ofb_crypt_mode
sha3_384
%zu bit rsa key\n
ccrc2_cbc_encrypt_mode
fipspost_post_hkdf
ccdh_gp_rfc3526group18
ccdes3_cfb8_decrypt_mode
ccmode_gcm_init
ccpad_cts2_encrypt
ccdh_import_priv
ccrc4
ccss_shamir_parameters_init
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n
cckem_encapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: HKDF with digest %s\n
ccxts_one_shot
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
ccdrbg_init
ccrng
ccec_verify_strict
d  = 0x
Attempt to copy x value of share out of share bag with invalid share index
AES_XTS_GENERIC
SHA512_VNG_INTEL_AVX2
ccaes_ofb_crypt_mode
3072
ccdes3_cbc_decrypt_mode
ccecies_encrypt_gcm
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES128 KAT\n
Z\xc9\xf7\xec8\xf6\x8bv#\x94\xd3\xca\xec륻
fipspost_post_rsa_oaep_kat_ws
ccshake256_xi
fipspost_post_ecdsa_kat_verify_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_init\n
ccec_cp_256
ccdrbg_factory_nisthmac
ccrsa_verify_pkcs1v15_digest
cckem_generate_key_with_seed
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed 2\n
ccrng failed assert cbc_info->block_size = %lu\n
ccrsa_sign_pss
fipspost_post_drbg_hmac
SHA384_VNG_ARM_HW
not implemented
ccdrbg_factory_nistctr
ccsha256_di
ccec_make_priv
ccspake_kex_generate
:
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n
ccrsa_sign_pkcs1v15
ccnistkdf_ctr_cmac_fixed
ccdes3_ofb_crypt_mode
ccrmd160_di
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_pub (P-%zu/SHA-%zu): %d\n
CCAES_KEY_SIZE_256
ccspake_cp_521
FIPSPOST_USER [%llu] %s:%d: FAILED: sig != expected signature\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv\n
fipspost_post_ecdsa_pairwise_ws
fipspost_get_hmac
FIPSPOST_USER [%llu] %s:%d: FAILED: len(plaintext) != len(message)\n
cccast_ecb_encrypt_mode
ccrsa_verify_pss_msg
ccdh_gp_rfc5114_MODP_2048_224
ccdes_ecb_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: TRACE: end: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-256): %d\n
cccast_ecb_decrypt_mode
ccmldsa_verify_with_context
sha3_224
ccec_verify_msg
roAhfqRBzTqHATLXmmLLiQIyBUchpmcqrXWMWoztGqWZrEbqIZFKWphBFbGkoJmnRaqDXZaYMreSUJhWTLypGstb
%s
cccast_cbc_encrypt_mode
ccrsa_verify_pss_digest
dp = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sig: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n
SHA384_VNG_INTEL_AVX1
ccdh_gp_rfc3526group17
ccrc2_cfb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_sign_pkcs1v15\n
fipspost_post_shake
fipspost_trace_end
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #32: %d\n
ccrsa_sign_pkcs1v15_msg
ccdes3_ecb_decrypt_mode
sha3_256
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_512 KAT\n
FIPSPOST_USER [%llu] %s:%d: TRACE: event: %s\n
SHA3_VNG_ARM_HW
ccaes_cbc_decrypt_mode
fipspost_post_ecdsa_sign_ws
ccblowfish_cbc_decrypt_mode
ccmd2_di
ccrc2_cfb8_encrypt_mode
SHA3_VNG_INTEL
ccrsa_decrypt_oaep
cced25519_make_key_pair
ccmd4_di
FIPSPOST_USER [%llu] %s:%d: [FIPSPOST][Module-ID] %s\n
Failed to generate a valid signature
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n
SHA384_VNG_INTEL_SUPPLEMENTAL_SSE3
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_pub\n
fipspost_post_indicator
qinv=0x
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch ek: %d\n
SHA384_LTC
ccmldsa_sign_with_context
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt encryption\n
cccbc_one_shot
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-384): %d\n
ccdh_compute_shared_secret
cckem_decapsulate
value to digest
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_384 KAT\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n
SHA256_VNG_INTEL_SUPPLEMENTAL_SSE3
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_384 KAT\n
ep i traffic
SHA256_VNG_INTEL_AVX2
User
ccaes_ctr_crypt_mode
ccnistkdf_ctr_cmac
SHA512_VNG_ARM
fipspost_post_rsa_oaep_decrypt_ws
ccec_cp_192
ccsha3_224_di
ccspake_kex_process
fipspost_post_rsa_verify
FIPSPOST_USER [%llu] %s:%d: FAILED: decrypt\n
AES_ECB_INTEL_OPT
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #79: %d\n
8192
ccdh_import_pub
full key %s { \n
cchpke_kem_generate_key_pair
priv: {
PpKpAmtfcDCPtAtwRMnHBueaQklIgpzLiH
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot decrypt\n
ccaes_gcm_decrypt_mode
ccss_shamir_share_generator_init
ccsha224_di
ccrsa_sign_pss_msg
42
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot encrypt\n
ccaes_cfb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: all tests PASSED (%u ms)\n
default
ccdh_gp_rfc5114_MODP_2048_256
cchpke
fipspost_run_post
fipspost_post_mlkem_encapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt one_shot\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n
cchpke_export_secret
%02X
FIPSPOST_USER [%llu] %s:%d: TRACE: integ_mac: 
\xf2f\xa1\x87
FIPSPOST_USER [%llu] %s:%d: FAILED: failed AES-CMAC KAT\n
ccspake_mac_hkdf_hmac_compute
ccrng_process_atfork_parent
ccrng_process_init
fipspost_post_mldsa_sign_rejection_kat_44
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_encrypt_oaep\n
ccdit_managed_context_begin MUST have been called
ccblowfish_cbc_encrypt_mode
fipspost_post_ecdh
fipspost_post_kdf_ctr
fipspost_post_mldsa_sign_kat
AES_ECB_INTEL_AESNI
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA256 KAT\n
ccdes3_cfb_encrypt_mode
sha3_512
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch pubkey: %d\n
cccast_cfb8_decrypt_mode
fipspost_post_ecdsa_verify_ws
UNKNOWN
AES_XTS_ARM
ccpad_cts3_decrypt
ccnistkdf_ctr_hmac_fixed
ccec_verify
fipspost_post_aes_ecb_decrypt
ccec_validate_pub
ccrc2_cfb_encrypt_mode
ccscrypt
ccmldsa65
?
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES256): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_df_bc_init\n
SeiPcvDyiAvRsPPKX
fipspost_post_ffdh_ws
ccec_cp_224
ccec_rfc6637_kdf
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES256 KAT\n
FIPSPOST_USER [%llu] %s:%d: MAC generated: 
ccsae_init
ccdrbg_generate
cced25519_verify
FIPSPOST_USER [%llu] %s:%d: TRACE: system_flags: %llx\n
ccaes_ecb_encrypt_mode
ccaes_cfb8_encrypt_mode
ccmd5_di
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-256): %d\n
ccdh_generate_key
cced25519_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: memcmp\n
sha512/256
P384-SHA512-SSWU-RO-
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_512 KAT\n
ccsigma_seal
ccmldsa87
wrap-sha512-kek-aes128
AES_XTS_INTEL_AESNI
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_224 KAT\n
24
Attempt to access y value of share out of share bag with invalid share index
ccsha3_512_di
ccrc2_ctr_crypt_mode
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv (P-%zu/SHA-%zu): %d\n
p  = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt cmp\n
ccmldsa_generate_key_with_seed
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n
SAE Hunting and Pecking
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-512): %d\n
fipspost_post_ecdsa
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA1 KAT\n
q  = 0x
fipspost_trace_call
FIPSPOST_USER [%llu] %s:%d: FAILED: AES-CBC KAT Failed %d\n
cchkdf
ccspake_cp_384
-POST_FAILURE: 0x%08X
SHA512_VNG_INTEL_SUPPLEMENTAL_SSE3
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #89: %d\n
ccdh_gp_apple768
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: FORCEFAIL\n
fipspost_post_aes_ccm
fipspost_post_rsa_sig
fipspost_post_aes_xts
fipspost_post_drbg_ctr
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt cmp\n
ccblowfish_ecb_encrypt_mode
ʃ\xd6E^\x98\xcd\t\xd6e\x86\xe2c\x92m\xe6
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n
ccaes_ccm_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_224 KAT\n
SHA1_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_SIG KAT #%zu\n
ccrsa_generate_fips186_key consistency
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sk: %d\n
SHA256_VNG_INTEL_AVX1
__text
ccsha3_384_di
ccrc2_ofb_crypt_mode
fipspost_post_ffdh_pairwise_ws
%s { %zu, 
ccdrbg_nistctr: invalid block size
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 1600-bit message failed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: could not create the hash\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-384): %d\n
ccecdh_generate_key
ccspake_mac_hkdf_derive
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_sign_msg (P-%zu/SHA-%zu): %d\n
FIPSPOST_USER [%llu] %s:%d:   In variable: 
FIPSPOST_USER [%llu] %s:%d: FAILED: rc: %d\n
fipspost_post_mlkem_keygen
SHA1_VNG_INTEL_AVX1
ccrsa_generate_fips186_key
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_full\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n
h\x8b\x9e(#+vT\xf95\x93\xa5\xc3\xf085
ccec_sign_msg
cckem_generate_key
fipspost_post_mldsa
corecrypto process rng
fipspost_post_mldsa_sign_rejection_kat
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA1 KAT\n
ccansikdf_x963
CCAES_KEY_SIZE_128
ccrsa_verify_pkcs1v15_msg
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt authentication\n
\xfa\f\xce\xd2.\x89k@
ccwrap_auth_decrypt_withiv
ccblowfish_cfb8_decrypt_mode
, z -> 
ccdrbg_nistctr: key length too long
\x9b\xc2\v)Q\xffr\xd3\xf2\x80\xff;\xd2\xdc=\xcc
fipspost_post_mldsa_verify_kat
FIPSPOST_USER [%llu] %s:%d: FAILED: plaintext != message\n
1024
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 1600-bit message failed\n
free ws
\xbe\xe1\x92\xef&ݻ#j\xf8)\xd0\xc7\xd8I\xb7
cc_clear
ccrc2_cfb8_decrypt_mode
sha256
FIPSPOST_USER [%llu] %s:%d: FAILED: digest: %s\n
fipspost_post_rsa_enc_dec
getentropy
fipspost_post_mlkem_pairwise
Software
ccaes_ccm_decrypt_mode
ccpad_cts2_decrypt
__TEXT
ccec_pairwise_consistency_check_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #0: %d\n
ccec_generate_key_fips
ccsigma_init
fipspost_post_ffdh
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA2 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n
ccec_make_pub
ccsha512_di
ccpbkdf2_hmac
dq = 0x
ccsigma_sign
ccdigest_internal
%.016llx
AES_ECB_ARM_ALIGNED
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA512 KAT\n
ccdrbg_done
ccec_sign
ccsae_init_p256_sha256
-POST_SUCCESS
ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n
cckem_mlkem1024
ccsigma_verify
fipspost_post_aes_cmac
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n
cced25519_sign: pk != sk * G
Digest should be at least 128 bits long: argument digest_len = %lu
```
