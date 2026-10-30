# `/usr/lib/system/libcorecrypto_trace.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,046,928 bytes.

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
cced25519_sign: pk != sk * G
Digest should be at least 128 bits long: argument digest_len = %lu
fipspost_post_mldsa_sign_kat
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n
ccec_rfc6637_unwrap_key
ccpad_cts2_decrypt
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n
fipspost_post_ecdsa_pairwise_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n
fipspost_post_mldsa_pairwise
ccsha512_256_di
free ws
cccbc_one_shot
ccec_pairwise_consistency_check_ws
ccdrbg_reseed
ccansikdf_x963
ccspake_mac_hkdf_hmac_sha512
ccaes_xts_decrypt_mode
ccdh_gp_rfc3526group18
ccpbkdf2_hmac
ccdes3_ctr_crypt_mode
fipspost_post_aes_ccm
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
ccec_cp_256
ccmd5_di
SHA1_VNG_INTEL_AVX2
ccaes_cfb_encrypt_mode
cced25519_sign
ccrsa_verify_pkcs1v15_digest
ccspake_cp_256
ccrc2_cfb8_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES256 KAT\n
FIPSPOST_USER [%llu] %s:%d: TRACE: fips_mode: %x\n
ccrsa_encrypt_oaep
cckem_encapsulate
cckem_mlkem768
cckem_generate_key
fipspost_post_ecdh
ccnistkdf_ctr_cmac
cchpke_kem_x25519_generate_key_pair
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-224): %d\n
ccnistkdf_ctr_cmac_fixed
ccsae_init
ccsigma_verify
__TEXT_EXEC
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #79: %d\n
ccsha3_224_di
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (s)\n
AES_XTS_ARM
ccblowfish_cbc_decrypt_mode
ccrc2_ecb_encrypt_mode
ccrsa_sign_pkcs1v15
}\n
p  = 0x
CCAES_KEY_SIZE_256
ccsha3_512_di
ccblowfish_ecb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed\n
SHA256_VNG_ARM
ccdes3_cbc_encrypt_mode
ccsae_init_p256_sha256
fipspost_post_kdf_ctr_cmac
sha3_256
m  = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n
AES_XTS_ARM_ALIGNED
Attempt to copy x value of share out of share bag with invalid share index
fipspost_post_aes_ecb_decrypt
SAE Hunting and Pecking
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA256 KAT\n
ccdh_gp_rfc3526group15
ccrng_process_atfork_child
fipspost_trace_start
SHA512_VNG_INTEL_SUPPLEMENTAL_SSE3
ccmode_gcm_init
ccec_rfc6637_kdf
cchpke_initiator_encrypt
fipspost_post_ffdh
ccrng_process_atfork_prepare
fipspost_post_mldsa_sign_rejection_kat_44
\xfa\f\xce\xd2.\x89k@
ccaes_ecb_decrypt_mode
3072
ccsigma_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
%s { %zu, 
cccmac_one_shot_verify
ccsha384_di
fipspost_post_rsa_verify
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt authentication\n
Failed to pick a random Miller-Rabin base
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-1): %d\n
ccrc2_cfb_encrypt_mode
ccrc2_cfb8_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_SIG KAT #%zu\n
ccss_shamir_share_generator_generate_share
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_224 KAT\n
P384-SHA512-SSWU-RO-
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n
AES_ECB_ARM
AES_ECB_TRNG
FIPSPOST_USER [%llu] %s:%d: FAILED: len(plaintext) != len(message)\n
ccaes_cbc_decrypt_mode
8192
cckem_decapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt one_shot\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot encrypt\n
ccmldsa_verify_prehashed
fipspost_get_hmac
SHA256_VNG_INTEL_AVX2
SHA3_VNG_INTEL
fipspost_post_shake
ccdigest_internal
ccdrbg_nistctr: invalid block size
sha3_224
ccspake_cp_521
sha3_384
ccdh_import_pub
cccast_ecb_decrypt_mode
ccdh_gp_rfc2409group05
ccmd2_di
ccspake_mac_hkdf_derive
NULL
fipspost_post_rsa_pairwise
SHA384_VNG_ARM_HW
ccrsa_generate_fips186_key
ccblowfish_cbc_encrypt_mode
cchpke
FIPSPOST_USER [%llu] %s:%d: TRACE: magic: %x\n
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt cmp\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-512): %d\n
INVALID Module ID
ccec_make_priv
ccdrbg_done
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_sign_pkcs1v15\n
SHA384_VNG_INTEL_AVX2
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_512 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv (P-%zu/SHA-%zu): %d\n
h\x8b\x9e(#+vT\xf95\x93\xa5\xc3\xf085
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_224 KAT\n
ccaes_ccm_encrypt_mode
ccrsa_decrypt_oaep
ccdh_gp_rfc2409group02
ccdh_gp_rfc5114_MODP_2048_224
cckem_mlkem1024
%zu bit rsa key\n
SHA1_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #0: %d\n
ccrsa_verify_pss_msg
wrap-sha256-kex-aes128wrap
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-384): %d\n
public key 
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_decrypt one_shot\n
SHA384_VNG_INTEL_AVX1
ccaes_xts_encrypt_mode
ccmldsa_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_384 KAT\n
fipspost_post_mlkem_encapsulate
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n
SHA512_VNG_INTEL_AVX1
ccaes_gcm_decrypt_mode
ccblowfish_ctr_crypt_mode
sha3_512
%02X
SHA256_LTC
SHA1_VNG_INTEL_AVX1
ccrsa_sign_pkcs1v15_msg
ccecies_encrypt_gcm
Anonymous Sender    
FIPSPOST_USER [%llu] %s:%d: FAILED: failed CMAC_AES128 KAT\n
ccmldsa_generate_key_with_seed
SeiPcvDyiAvRsPPKX
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n
AES_ECB_ARM_ALIGNED
ccrc2_ecb_decrypt_mode
q  = 0x
ccrsa_sign_pss
ccdes_ecb_encrypt_mode
ccmldsa_verify
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_256 KAT\n
27.0
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA2 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_extract_rs (P-%zu/SHA-%zu): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_priv\n
corecrypto process rng
ccspake_cp_384
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES256): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: rc: %d\n
UNKNOWN
FIPSPOST_USER [%llu] %s:%d: FAILED: memcmp\n
ccss_shamir_poly_coefficient with index bigger than or equal to threshold
ccec_cp_384
ccss_shamir_parameters_init
fipspost_post_ecdsa
e  = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_consistency\n
, y -> 
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-1): %d\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n
SHA256_VNG_INTEL_SUPPLEMENTAL_SSE3
fipspost_post_rsa_oaep_consistency_ws
Apple corecrypto Module
ccwrap_auth_encrypt_withiv
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCRSA_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n
fipspost_trace_call
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n
, z -> 
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-512): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n
32
cchkdf
cccast_cbc_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_compute_shared_secret\n
FIPSPOST_USER [%llu] %s:%d: all tests PASSED (%u ms)\n
fipspost_post_ecdsa_sign_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: decrypt\n
AES_ECB_LTC
ccdrbg_factory_nisthmac
ccblowfish_cfb_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt encryption\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-512): %d\n
ccdes3_ecb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_VER KAT #%zu\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_x963_import_pub (P-%zu/SHA-%zu): %d\n
ccdes3_cfb8_decrypt_mode
ccmd4_di
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #2: %d\n
cccast_cfb_encrypt_mode
ccecies_decrypt_gcm
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sk: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch sig: %d\n
SHA256_VNG_ARM_ALIGNED
ccsae_get_keys
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_full\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n
Apple ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_verify_pkcs1v15\n
sha512
alloc ws
fipspost_post_mldsa_verify_kat
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_encrypt_oaep\n
ccaes_cbc_encrypt_mode
ccsigma_init
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_sign_msg (P-%zu/SHA-%zu): %d\n
fipspost_post_mlkem_keygen
ccsha1_di
ccec_cp_224
ccdh_generate_key
fipspost_post_pbkdf
ccrng failed assert cbc_info->block_size = %lu\n
ccdrbg_factory_nistctr
ccdh_gp_rfc5114_MODP_1024_160
priv: {
User
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #32: %d\n
cccast_ecb_encrypt_mode
ccgcm_one_shot
ccdh_gp_rfc3526group14
ccdes3_cfb_encrypt_mode
value to digest
AES_XTS_GENERIC
SHA512_VNG_ARM
%s
ccwrap_auth_decrypt_withiv
ccpad_cts2_encrypt
ccspake_mac_hkdf_hmac_sha256
ccss_shamir_share_generator_init
ccmldsa_generate_key
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n
\xf2f\xa1\x87
ccec_verify_msg
ccblowfish_cfb8_encrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected FAILURE\n
ep i traffic
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-512): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_512 KAT\n
fipspost_post_indicator
fipspost_post_aes_xts
fipspost_post
fipspost_post_ecdh_ws
-
SHA384_VNG_INTEL_SUPPLEMENTAL_SSE3
fipspost_post_rsa_oaep_decrypt_ws
ccecdh_generate_key
fipspost_post_aes_gcm
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (r)\n
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 0-bit message failed\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n
SHA256_VNG_INTEL_AVX1
SHA256_ARMV6M
cccast_cfb8_encrypt_mode
fipspost_post_rsa_sig
sha256
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n
fipspost_post_mldsa_sign_rejection_kat
SHA3_C
SHA3_VNG_ARM
6144
ccnistkdf_ctr_hmac
ccnistkdf_ctr_hmac_fixed
cch2c
cchpke_responder_decrypt
cchpke_export_secret
ccsae_ctr_hmac_fixed
FIPSPOST_USER [%llu] %s:%d: FAILED: sig != expected signature\n
ccdes3_cfb_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-384): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n
SHA512_VNG_INTEL_AVX2
cchmac
ccrsa_sign_pss_msg
ccblowfish_ecb_encrypt_mode
ccrc2_ctr_crypt_mode
FIPSPOST_USER [%llu] %s:%d: MAC generated: 
FIPSPOST_USER [%llu] %s:%d:   In variable: 
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n
cc_clear
ccscrypt
fipspost_post_ffdh_pairwise_ws
Failed to generate random
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA1 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_reseed 2\n
d  = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCDH_PAIRWISE_CONSISTENCY: FORCEFAIL\n
Software
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt decryption\n
fipspost_post_rsa_enc_dec
\x9b\xc2\v)Q\xffr\xd3\xf2\x80\xff;\xd2\xdc=\xcc
ccrng failed assert key_nbytes = %lu\n
SHA384_VNG_ARM
FIPSPOST_USER [%llu] %s:%d: FAILED: plaintext != message\n
P256-SHA256-SSWU-RO-
P521-SHA512-SSWU-RO-
ccdit_managed_context_begin MUST have been called
ccec_generate_key_fips consistency
ʃ\xd6E^\x98\xcd\t\xd6e\x86\xe2c\x92m\xe6
-POST_SUCCESS
fipspost_post_integrity
CCAES_KEY_SIZE_128
__text
SHA512_VNG_ARM_HW
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_decrypt_oaep\n
ccaes_ctr_crypt_mode
16
1024
cccast_cfb_decrypt_mode
ccec_sign
AES_XTS_INTEL_OPT
SHA1_VNG_INTEL_SUPPLEMENTAL_SSE3
ccaes_ccm_decrypt_mode
ccrng_generate
ccrng_process_atfork_parent
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: FORCEFAIL\n
cchmac_internal
ccdh_gp_rfc3526group17
ccec_rfc6637_wrap_key
FIPSPOST_USER [%llu] %s:%d: [PCT] CCRSA_PAIRWISE_CONSISTENCY: FORCEFAIL\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccec_verify_msg (P-%zu/SHA-%zu): %d\n
cccbc_one_shot_explicit_internal
qinv=0x
ccdes3_ofb_crypt_mode
ccmldsa_verify_with_context
fipspost_post_ecdsa_kat_verify_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA3_256 KAT\n
dq = 0x
FIPSPOST_USER [%llu] %s:%d: FAILED: test %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccgcm_one_shot decrypt\n
ccrc2_cfb_decrypt_mode
fipspost_post_ecdsa_kat_sign_ws
sha512/256
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate\n
ccaes_gcm_encrypt_mode
fipspost_post_mldsa
%.016llx
FIPSPOST_USER [%llu] %s:%d: FAILED: encrypt\n
ccrc4
FIPSPOST_USER [%llu] %s:%d: FAILED: digest: %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: HKDF with digest %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #47: %d\n
ccpad_cts3_decrypt
ccdh_import_priv
ccshake128_xi
ccrc2_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: TRACE: end: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #89: %d\n
ccspake_kex_process
ccdrbg_nistctr: key length too long
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-256): %d\n
SHA384_LTC
ccxts_one_shot
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA3-256): %d\n
not implemented
-POST_FAILURE: 0x%08X
AES_XTS_INTEL_AESNI
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES128): %d\n
ccrsa_generate_fips186_key consistency
fipspost_trace_end
fipspost_post_mlkem_decapsulate
ccdes3_cfb8_encrypt_mode
ccec_verify
ccrng_process_init
Attempt to access y value of share out of share bag with invalid share index
FIPSPOST_USER [%llu] %s:%d: FAILED: aes_ecb_encrypt cmp\n
AES_ECB_SKG
cccast_cbc_decrypt_mode
cced25519_make_key_pair
FIPSPOST_USER [%llu] %s:%d: FAILED: ccccm_one_shot encrypt authentication\n
fipspost_run_post
ccec_cp_192
ccdes3_cbc_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch privkey: %d\n
4096
ccrc2_cbc_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_df_bc_init\n
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n
ccaes_cfb8_decrypt_mode
FIPSPOST_USER [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: result: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccrsa_import_priv\n
ccpad_cts1_decrypt
ccec_cp_521
fipspost_post_mlkem
ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n
ccdh_compute_shared_secret
ccdes3_ecb_encrypt_mode
ccdh_gp_rfc5114_MODP_2048_256
ccpad_cts3_encrypt
ccrc2_cbc_encrypt_mode
ccmldsa87
fipspost_post_ffdh_ws
ep r traffic
fipspost_post_mldsa_keygen
ccsha224_di
ccshake256_xi
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdh_import_pub\n
__TEXT
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch ek: %d\n
AES_ECB_INTEL_AESNI
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA1 KAT\n
ccblowfish_cfb8_decrypt_mode
%s { x -> 
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 1600-bit message failed\n
SHA256_VNG_ARM64_NEON
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCDH_PAIRWISE_CONSISTENCY: Unexpected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_generate 2\n
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n
ccmldsa65
fipspost_post_aes_cmac
:
FIPSPOST_USER [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-256): %d\n
ccaes_cfb8_encrypt_mode
ccrsa_verify_pkcs1v15_msg
ccmldsa_sign_prehashed
fipspost_post_ecdsa_verify_ws
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE256, 1600-bit message failed\n
cckem_generate_key_with_seed
fipspost_post_mlkem_pairwise
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA512 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed HMAC_SHA3_384 KAT\n
FIPSPOST_USER [%llu] %s:%d: FAILED: failed AES-CMAC KAT\n
ccpad_cts1_encrypt
ccblowfish_cfb_decrypt_mode
fipspost_post_aes_cbc
Failed to generate a valid signature
ccmode_gcm_decrypt
FIPSPOST_USER [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: AES-CBC KAT Failed %d\n
ccsha256_di
ccsrp_gp_rfc5054_2048
42
PpKpAmtfcDCPtAtwRMnHBueaQklIgpzLiH
ccec_make_pub
ccaes_ecb_encrypt_mode
ccblowfish_ofb_crypt_mode
FIPSPOST_USER [%llu] %s:%d: [FIPSPOST][Module-ID] %s\n
FIPSPOST_USER [%llu] %s:%d: FAILED: %s: %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n
ccrng
sha1
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-256): %d\n
FIPSPOST_USER [%llu] %s:%d: FAILED: ccdrbg_init\n
2048
ccec_verify_strict
ccspake_mac_hkdf_cmac_aes128_sha256
fipspost_post_drbg_hmac
full key %s { \n
ccrsa_eme_pkcs1v15_decode_generate_random
cced25519_verify
ccrsa_verify_pss_digest
dp = 0x
ccaes_cfb_decrypt_mode
ccdh_gp_apple768
ccspake_mac_hkdf_hmac_compute
ccmldsa_sign_with_context
fipspost_post_rsa_sign
FIPSPOST_USER [%llu] %s:%d: FAILED: mismatch pubkey: %d\n
fipspost_post_aes_ecb_encrypt
AES_ECB_INTEL_OPT
cccast_ofb_crypt_mode
fipspost_post_hkdf
SAE KCK and PMK
ccec_sign_msg
fipspost_post_drbg_ctr
com.apple.corecrypto
FIPSPOST_USER [%llu] %s:%d: TRACE: event: %s\n
ccaes_ofb_crypt_mode
24
ccec_generate_key_fips
FIPSPOST_USER [%llu] %s:%d: FAILED: SHAKE128, 0-bit message failed\n
secret-key
Z\xc9\xf7\xec8\xf6\x8bv#\x94\xd3\xca\xec륻
cccmac_one_shot_generate
ccdrbg_init
ccsha3_256_di
cccast_ctr_crypt_mode
FIPSPOST_USER [%llu] %s:%d: FAILED: could not create the hash\n
ccsigma_seal
wrap-sha512-kek-aes128
fipspost_post_aes_ecb
pubkey:
getentropy
%s v%s [%s, %s, %s, %s, %s]
ccdrbg_generate
ccdh_gp_rfc3526group16
cchpke_kem_generate_key_pair
SHA1_LTC
ccsha3_384_di
ccrmd160_di
fipspost_post_hmac
\xbe\xe1\x92\xef&ݻ#j\xf8)\xd0\xc7\xd8I\xb7
FIPSPOST_USER [%llu] %s:%d: TRACE: version: %x\n
cccast_cfb8_decrypt_mode
ccspake_kex_generate
FIPSPOST_USER [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA3-224): %d\n
SHA512_LTC
fipspost_post_rsa_oaep_kat_ws
ccsha512_di
FIPSPOST_USER [%llu] %s:%d: TRACE: integ_mac: 
FIPSPOST_USER [%llu] %s:%d: TRACE: system_flags: %llx\n
ccec_validate_pub
ccecdh_compute_shared_secret
ccrng_uniform
M\xac%]
fipspost_post_kdf_ctr
roAhfqRBzTqHATLXmmLLiQIyBUchpmcqrXWMWoztGqWZrEbqIZFKWphBFbGkoJmnRaqDXZaYMreSUJhWTLypGstb
FIPSPOST_USER [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n
SHA3_VNG_ARM_HW
FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_rsa_oaep_kat\n
?
FIPSPOST_USER [%llu] %s:%d: FAILED: failed PBKDF_SHA512 KAT\n
default
```
