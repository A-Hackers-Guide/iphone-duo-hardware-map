# `com.apple.kec.corecrypto`

- Name: corecrypto
- Version: `27.0`
- UUID: `FFD6989E-0F1D-38F9-A6D0-5CE27102B62B`
- Source version: `2109.40.22.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 12.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 11.2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 11.2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 11.2, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 11.2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00014d70 off=0x00e026d0-0x00e17440 addr=0xfffffe0007e066d0-0xfffffe0007e1b440 r--/r--   __TEXT            
	sz=0x0000453c off=0x00e02cf8-0x00e07234 addr=0xfffffe0007e06cf8-0xfffffe0007e0b234               __TEXT.__cstring          (CstringLiterals)
	sz=0x000101e0 off=0x00e07240-0x00e17420 addr=0xfffffe0007e0b240-0xfffffe0007e1b420               __TEXT.__const            
	sz=0x00000020 off=0x00e17420-0x00e17440 addr=0xfffffe0007e1b420-0xfffffe0007e1b440               __TEXT.__fips_hmacs       
001: LC_SEGMENT_64 sz=0x0006d558 off=0x03b28240-0x03b95798 addr=0xfffffe000ab2c240-0xfffffe000ab99798 r-x/r-x   __TEXT_EXEC       
	sz=0x0006d328 off=0x03b28240-0x03b95568 addr=0xfffffe000ab2c240-0xfffffe000ab99568          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000230 off=0x03b95568-0x03b95798 addr=0xfffffe000ab99568-0xfffffe000ab99798          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00004000 off=0x04a37b00-0x04a3bb00 addr=0xfffffe000ba3bb00-0xfffffe000ba40cb8 rw-/rw-   __DATA            
	sz=0x000029e0 off=0x04a37b00-0x04a3a4e0 addr=0xfffffe000ba3bb00-0xfffffe000ba3e4e0               __DATA.__data             
	sz=0x000027c0 off=0x00000000-0x000027c0 addr=0xfffffe000ba3e4e0-0xfffffe000ba40ca0               __DATA.__bss              (Zerofill)
	sz=0x00000018 off=0x00000000-0x00000018 addr=0xfffffe000ba40ca0-0xfffffe000ba40cb8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00004288 off=0x014bae00-0x014bf088 addr=0xfffffe00084bee00-0xfffffe00084c3088 rw-/rw-   __DATA_CONST      
	sz=0x00003fd8 off=0x014bae00-0x014bedd8 addr=0xfffffe00084bee00-0xfffffe00084c2dd8         __DATA_CONST.__const            
	sz=0x00000118 off=0x014bedd8-0x014beef0 addr=0xfffffe00084c2dd8-0xfffffe00084c2ef0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000010 off=0x014beef0-0x014bef00 addr=0xfffffe00084c2ef0-0xfffffe00084c2f00         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000188 off=0x014bef00-0x014bf088 addr=0xfffffe00084c2f00-0xfffffe00084c3088         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 72 at 0x04b0005c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FFD6989E-0F1D-38F9-A6D0-5CE27102B62B
008: LC_SOURCE_VERSION           2109.40.22.0.0
009: LC_FUNCTION_STARTS          offset=0x004ace338 size=0xbc8
```

## Info.plist keys [KC]

- `AppleKernelExternalComponent`: `True`
- `AppleNeedsTEXTSegmentHash`: `True`
- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `corecrypto`
- `CFBundleIdentifier`: `com.apple.kec.corecrypto`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `corecrypto`
- `CFBundleNumericVersion`: `654344192`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `27.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `27.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2012 Apple Inc. All rights reserved.`
- `OSBundleAllowUserLoad`: `True`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `OSKextVariantOverride`:
  - `rpi3`: `_noasm`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/corecrypto.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891108656`
- `_PrelinkExecutableRelativePath`: `corecrypto`
- `_PrelinkExecutableSize`: `571144`
- `_PrelinkExecutableSourceAddr`: `-2198891108656`
- `_PrelinkKmodInfo`: `-2198827975936`

## Strings (371) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ccdrbg_factory_nisthmac`
- `ccsha512_di`
- `ccec_cp_256`
- `ccec_cp_384`
- `ccsha224_di`
- `ccshake256_xi`
- `ccmd5_di`
- `ccblowfish_cbc_decrypt_mode`
- `ccdes3_ctr_crypt_mode`
- `fipspost_post_pbkdf`
- `sha1`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: sig != expected signature\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-256): %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-1): %d\n`
- `ccdes3_cbc_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_SIG KAT #%zu\n`
- `fipspost_post_ecdsa_verify_ws`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate: %d\n`
- `PpKpAmtfcDCPtAtwRMnHBueaQklIgpzLiH`
- `Apple ARM`
- `cced25519_sign`
- `fipspost_post_mldsa_sign_kat`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #47: %d\n`
- `ccentropy_digest_init`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed HMAC_SHA256 KAT\n`
- `ccrng_uniform`
- `ccaes_ccm_encrypt_mode`
- `ccsha3_224_di`
- `ccrc2_ecb_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_init\n`
- `ccaes_cfb8_encrypt_mode`
- `cc_abort.c`
- `ccdrbg_init`
- `ccec_sign`
- `ccrc2_ofb_crypt_mode`
- `ccdes_ecb_encrypt_mode`
- `fipspost_post_kdf_ctr_cmac`
- `fipspost_get_hmac`
- `fipspost_post_aes_ecb_encrypt`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_sign_msg (P-%zu/SHA-%zu): %d\n`
- `ccecies_decrypt_gcm`
- `ccaes_gcm_decrypt_mode`
- `ccdrbg_generate`
- `ccrc4`
- `cckem_decapsulate`
- `ccmldsa_generate_key`
- `fipspost_post_aes_cmac`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: aes_ecb_decrypt cmp\n`
- `fipspost_post_ecdsa_sign_ws`
- `ccrng failed assert cbc_info->block_size = %lu\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid privkey_kat: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed AES-CMAC KAT\n`
- `\xfa\f\xce\xd2.\x89k@`
- `ccrc2_ecb_decrypt_mode`
- `ccrmd160_di`
- `ccmldsa_generate_key_with_seed`
- `fipspost_post_ecdsa_kat_sign_ws`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected FAILURE\n`
- `PPL cc_malloc trying to allocate larger than PAGE_SIZE`
- `ccec_verify_msg`
- `cccast_ofb_crypt_mode`
- `ccsrp_gp_rfc5054_2048`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu_VER KAT #%zu\n`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: expected SUCCESS\n`
- `ccaes_cfb_encrypt_mode`
- `2048`
- `ccblowfish_ecb_decrypt_mode`
- `ccblowfish_cfb_encrypt_mode`
- `cced25519_make_key_pair`
- `fipspost_post_aes_ecb`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed PBKDF_SHA1 KAT\n`
- `Error reseeding kernel rng`
- `cc_kext_random_kmem_init: ccrng_crypto_init()`
- `ccaes_ecb_encrypt_mode`
- `ccdes3_cfb8_encrypt_mode`
- `ccmd2_di`
- `ccrsa_verify_pss_digest`
- `ccrsa_verify_pss_msg`
- `cccast_cfb_decrypt_mode`
- `ccdes3_cfb_encrypt_mode`
- `fipspost_post_aes_ecb_decrypt`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: FORCEFAIL\n`
- `ccdes3_ecb_decrypt_mode`
- `ccmldsa_verify`
- `fipspost_post_mlkem_pairwise`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt decryption\n`
- `ccsha3_384_di`
- `ccrsa_sign_pss_msg`
- `ccansikdf_x963`
- `ccmldsa_sign_prehashed`
- `free ws`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed HMAC_SHA512 KAT\n`
- `corecrypto_kext_start completed successfully\n`
- `ccdes3_cfb8_decrypt_mode`
- `ccrc2_cfb8_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: PASSED: (%u ms) - %s\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: %s: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: encrypt\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: aes_ecb_encrypt one_shot\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCEC_PAIRWISE_CONSISTENCY: unexpected SUCCESS\n`
- `ccaes_cfb8_decrypt_mode`
- `\xf2f\xa1\x87`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed PBKDF_SHA512 KAT\n`
- `ccdit_managed_context_begin MUST have been called`
- `ccec_make_pub`
- `cccast_cbc_encrypt_mode`
- `ccrc2_cbc_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: result: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid sk_kat: %d\n`
- `fipspost_post_mldsa_keygen`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed HMAC_SHA1 KAT\n`
- `27.0`
- `fipspost_run_post`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: AES-CBC KAT Failed %d\n`
- `ccaes_cbc_encrypt_mode`
- `cccast_cfb8_decrypt_mode`
- `cckem_generate_key_with_seed`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_derive_key_from_seed: %d\n`
- `ccentropy_lock_init`
- `ccrsa_generate_fips186_key consistency`
- `ccrng_generate`
- `ccscrypt`
- `fipspost_post_mlkem_keygen`
- `M\xac%]`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: FORCEFAIL\n`
- `:`
- `cccmac_one_shot_generate`
- `ccblowfish_cfb8_encrypt_mode`
- `fipspost_post_rsa_sign`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected SUCCESS\n`
- `ccpad_cts3_decrypt`
- `ccdes3_cbc_decrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed PBKDF_SHA2 KAT\n`
- `\n`
- `fipspost_post_aes_xts`
- `FIPSPOST_KEXT [%llu] %s:%d: all tests PASSED (%u ms)\n`
- `RX\xdd\xefK\xdaB\xedI\x9eW\xf1Qt\xb0\x87`
- `ccrng_fortuna`
- `\"FIPS Kernel POST Failed (%d)!\" @%s:%d`
- `cccmac_one_shot_verify`
- `cccast_cbc_decrypt_mode`
- `ccrc2_cfb_decrypt_mode`
- `fipspost_post_aes_ccm`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: aes_ecb_encrypt cmp\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: rc: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: expected SUCCESS\n`
- `corecrypto_kext_start (tracing disabled)\n`
- `cccast_ecb_decrypt_mode`
- `cckem_mlkem1024`
- `fipspost_post_rsa_sig`
- `fipspost_post`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch ek: %d\n`
- `fipspost_post_mldsa_verify_kat`
- `ccdrbg_df_bc_init`
- `ccsha3_512_di`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: test %d\n`
- `fipspost_post_ecdh_ws`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (s)\n`
- `CCAES_KEY_SIZE_128`
- `fipspost_post_hkdf`
- `fipspost_post_drbg_hmac`
- `PPL cc_free trying to free larger than PAGE_SIZE`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES128): %d\n`
- `ccaes_gcm_encrypt_mode`
- `1024`
- `4096`
- `ccrsa_generate_fips186_key`
- `ccrsa_encrypt_oaep`
- `fipspost_post_indicator`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_x963_import_pub (P-%zu/SHA-%zu): %d\n`
- `sha256`
- `ccsha3_256_di`
- `ccmldsa_sign_with_context`
- `FIPSPOST_KEXT [%llu] %s:%d: [FIPSPOST][Module-ID] %s\n`
- `fipspost_post_ecdsa_kat_verify_ws`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid pubkey_kat: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected FAILURE: %d\n`
- `Panic context cc_malloc trying to allocate larger than PANIC_SCRATCH_BUFFER_SIZE`
- `cc_kext_random_uniform: ccrng_uniform()`
- `ccec_cp_521`
- `ccshake128_xi`
- `__text`
- `fipspost_post_mldsa_pairwise`
- `Apple corecrypto Module`
- `ccrc2_cfb_encrypt_mode`
- `ccrsa_decrypt_oaep`
- `SeiPcvDyiAvRsPPKX`
- `%02X`
- `fipspost_post_kdf_ctr`
- `N/A`
- `value to digest`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch pubkey: %d\n`
- `Panic context cc_malloc trying to allocate twice from panic_scratch_buffer`
- `ccec_generate_key_fips consistency`
- `ccaes_xts_encrypt_mode`
- `ccrsa_sign_pss`
- `fipspost_post_ecdsa`
- `\x9b\xc2\v)Q\xffr\xd3\xf2\x80\xff;\xd2\xdc=\xcc`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCEC_PAIRWISE_CONSISTENCY: FORCEFAIL\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccrsa_verify_pkcs1v15\n`
- `fipspost_post_mldsa_sign_rejection_kat`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection): %d\n`
- `ccec_make_priv`
- `ccmldsa_verify_prehashed`
- `sha512`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccccm_one_shot AEAD decrypt authentication\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #89: %d\n`
- `\"%s\" @%s:%d`
- `ccdrbg_factory_nistctr`
- `ccdrbg_done`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_reseed\n`
- `Failure to initialize ccrng_crypto`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_extract_rs (P-%zu/SHA-%zu): %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #79: %d\n`
- `not implemented`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed CMAC_AES256 KAT\n`
- `ccaes_cbc_decrypt_mode`
- `ccwrap_auth_encrypt_withiv`
- `ccblowfish_cfb8_decrypt_mode`
- `cccast_cfb_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: aes_ecb_decrypt one_shot\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch sk: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_verify: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: unexpected FAILURE: %d\n`
- `cccast_ecb_encrypt_mode`
- `ccrsa_verify_pkcs1v15_digest`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_privkey: %d\n`
- `ccrsa_eme_pkcs1v15_decode_generate_random`
- `%s v%s [%s, %s, %s, %s, %s]`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed CMAC_AES128 KAT\n`
- `corecrypto process rng`
- `cc_kext_random_kmem_init: ccrng_generate()`
- `3072`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: HKDF with digest %s\n`
- `ccaes_cfb_decrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #0: %d\n`
- `fipspost_post_aes_gcm`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch privkey: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_encapsulate_msg: %d\n`
- `roAhfqRBzTqHATLXmmLLiQIyBUchpmcqrXWMWoztGqWZrEbqIZFKWphBFbGkoJmnRaqDXZaYMreSUJhWTLypGstb`
- `corecrypto_kext.c`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_generate COUNT #32: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-1): %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_cmac_fixed (AES256): %d\n`
- `ccaes_ccm_decrypt_mode`
- `ccblowfish_cfb_decrypt_mode`
- `ccec_verify`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccgcm_one_shot encrypt\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_export_pubkey: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign (rejection, ML-DSA-44): %d\n`
- `cckprng_generate`
- `SL1`
- `ccrng`
- `cchmac`
- `NULL`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: Invalid ek_kat: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-256): %d\n`
- `ccsha512_256_di`
- `ccdes3_ecb_encrypt_mode`
- `\xbe\xe1\x92\xef&ݻ#j\xf8)\xd0\xc7\xd8I\xb7`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ECDSA_P%zu_SHA%zu KAT (r)\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_decapsulate_masked: %d\n`
- `ccwrap_auth_decrypt_withiv`
- `ccec_sign_msg`
- `ccdes3_cfb_decrypt_mode`
- `cckem_encapsulate`
- `fipspost_post_hmac`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: memcmp\n`
- `fipspost_post_rsa_verify`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccpbkdf2_hmac (SHA-512): %d\n`
- `cchkdf`
- `ccblowfish_ofb_crypt_mode`
- `42`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: could not create the hash\n`
- `fipspost_post_aes_cbc`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_generate 2\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_verify_msg (P-%zu/SHA-%zu): %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: [PCT] CCMLDSA_KEYGEN_PAIRWISE_CHECK: expected SUCCESS\n`
- `ccmd4_di`
- `ccmldsa_sign`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccccm_one_shot encrypt authentication\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccnistkdf_ctr_hmac_fixed (SHA-512): %d\n`
- `INVALID Module ID`
- `ccsha384_di`
- `ccsha1_di`
- `cckem_mlkem768`
- `cc_lock_init`
- `ccrng_fortuna_generate: Maximum request size exceeded`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_generate\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_reseed 2\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_x963_import_priv\n`
- `ccaes_ctr_crypt_mode`
- `ccdrbg_reseed`
- `ccdh_compute_shared_secret`
- `ccrc2_cfb8_decrypt_mode`
- `fipspost_post_drbg_ctr`
- `CCAES_KEY_SIZE_256`
- `ccsha256_di`
- `ccec_cp_224`
- `cccast_ctr_crypt_mode`
- `ccmldsa_verify_with_context`
- `FIPSPOST_KEXT [%llu] %s:%d:   In variable: `
- `__TEXT`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: unable to acquire mach header\n`
- `sha512/256`
- `fipspost_post_mlkem_encapsulate`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_export_privkey: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_import_pubkey: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig: %d\n`
- `Failed to generate a valid signature`
- `ccdrbg_nistctr: key length too long`
- `corecrypto kext rng`
- `fipspost_post_ecdsa_pairwise_ws`
- `ccec_cp_192`
- `ccec_validate_pub`
- `ccrsa_sign_pkcs1v15_msg`
- `cccast_cfb8_encrypt_mode`
- `ccrsa_sign_pkcs1v15`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccccm_one_shot encrypt encryption\n`
- `fipspost_post_mldsa_sign_rejection_kat_44`
- `ccecies_encrypt_gcm`
- `fipspost_post_ecdh`
- `ʃ\xd6E^\x98\xcd\t\xd6e\x86\xe2c\x92m\xe6`
- `ccentropy_add_entropy`
- `fips_mode`
- `ccblowfish_ctr_crypt_mode`
- `fipspost_post_mlkem_decapsulate`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch rejection sig (ML-DSA-44): %d\n`
- `Failure to instantiate drbg`
- `ccpbkdf2_hmac`
- `ccrc2_cbc_decrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccgcm_one_shot decrypt\n`
- `ccrng failed assert key_nbytes = %lu\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: [PCT] CCMLKEM_KEM_PAIRWISE_CHECK: unexpected SUCCESS\n`
- `corecrypto kext first entropy seed`
- `ccec_generate_key_fips`
- `ccrsa_verify_pkcs1v15_msg`
- `ccdes3_ofb_crypt_mode`
- `cckem_generate_key`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: digest: %s\n`
- `ccrng failed assert sizeof(ctx->cbc_ctx) >= cbc_info->size, %lu >= %lu\n`
- `ccmldsa65`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmlkem_kem_keypair_from_seed: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed cccmac_one_shot_verify COUNT #2: %d\n`
- `%s`
- `ccmldsa87`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: decrypt\n`
- `Software`
- `fipspost_post_integrity`
- `ccblowfish_ecb_encrypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: MAC generated: `
- `__TEXT_EXEC`
- `alloc ws`
- `cc_kext_random_generate: ccrng_generate()`
- `ccpad_cts3_encrypt`
- `ccblowfish_cbc_encrypt_mode`
- `cced25519_verify`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: failed ccec_x963_import_priv (P-%zu/SHA-%zu): %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccrsa_sign_pkcs1v15\n`
- `ccaes_ofb_crypt_mode`
- `ccdrbg_nistctr: invalid block size`
- `ccentropy_list_init`
- `ccec_verify_strict`
- `ccrc2_ctr_crypt_mode`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccdrbg_df_bc_init\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: ccmldsa_sign: %d\n`
- `FIPSPOST_KEXT [%llu] %s:%d: FAILED: mismatch sig: %d\n`
- `ccentropy_rng_init`
- `Kernel`
- `ccaes_ecb_decrypt_mode`
- `ccaes_xts_decrypt_mode`
