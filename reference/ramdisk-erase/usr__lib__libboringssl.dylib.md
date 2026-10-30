# `/usr/lib/libboringssl.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,724,848 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 4240)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (10)

- `/usr/lib/libboringssl.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Network.framework/Network (compatibility version 1.0.0, current version 6681.52.5)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (8 classes, 9 protocols)

Classes: `boringssl_concrete_boringssl_context_state`, `boringssl_concrete_boringssl_ctx`, `boringssl_concrete_boringssl_identity`, `boringssl_concrete_boringssl_psk`, `boringssl_concrete_boringssl_psk_cache`, `boringssl_concrete_boringssl_session_cache`, `boringssl_concrete_boringssl_session_state`, `boringssl_concrete_nw_protocol_boringssl`

Protocols: `NSObject`, `OS_boringssl_context_state`, `OS_boringssl_ctx`, `OS_boringssl_identity`, `OS_boringssl_psk`, `OS_boringssl_psk_cache`, `OS_boringssl_session_cache`, `OS_boringssl_session_state`, `OS_nw_protocol_boringssl`

## Strings (3,745)

First 2,500 of 3,745.
```
%{public}s(%d) %{public}s[%p] secret_len: %zu, identity_len: %zu
%{public}s(%d) %{public}s[%p] Failed to allocate %d bytes for input_buffer
%{public}s(%d) %{public}s[%p] boringssl_session_set_peer_hostname(%{public}s) failed
%{public}s(%d) RSA_decrypt not implemented
%{public}s(%d) EVP_CIPH_ECB_MODE not implemented
%{public}s(%d) %{public}s[%p] Performing local ATS trust evaluation
%{public}s(%d) %{public}s[%p] updating read secret. Level: %u, secret_data_length: %zu urrently negotiated ciphersuite: %u
%{public}s(%d) %{public}s[%p] boringssl_session_state_create failed
%{public}s(%d) %{public}s[%p] EAP key material computation failed
%{public}s(%d) %{public}s[%p] Cannot copy frame, buffer=%p length=%u
%{public}s(%d) %{public}s[%p] Waiting for writable frames -- returning 0 frames
%{public}s(%d) %{public}s[%p] boringssl_helper_create_buffer_from_dispatch_data failed
%{public}s(%d) %{public}s[%p] SSL_shutdown returned. Disconnect successful? %@
%{public}s(%d) %{public}s[%p] Server looking up PSK using non-NULL client identity
%{public}s(%d) %{public}s[%p] no batching frames available; requested min=%d, max=%u
%{public}s(%d) %{public}s[%p] nw_protocol_get_input_frames(%s) is not valid
%{public}s(%d) %{public}s[%p] parameters is nil
%{public}s(%d) %{public}s[%p] Invoking client PSK selection callback.
%{public}s(%d) %{public}s[%p] Unexpected EAP method
%{public}s(%d) cckem_export_pubkey failed
%{public}s(%d) Failed to allocate a boringssl session state object.
%{public}s(%d) %{public}s[%p] Unexpected peer public key type: %ld for server: %{public}s
%{public}s(%d) %{public}s[%p] Verification already in progress
%{public}s(%d) %{public}s[%p] total bytes read: %u
nw_protocol_boringssl_disconnect has been called re-entrantly, returning early to avoid double disconnect.
%{public}s(%d) %{public}s[%p] Lower protocol stack error during TLS handshake. [%d: %s]
%{public}s(%d) %{public}s[%p] Error: %{public}s
%{public}s(%d) %{public}s[%p] Server looking up PSK without identity
%{public}s(%d) %{public}s[%p] default_input_handler is NULL
%{public}s(%d) Key size %zui is not supported for ECDH.
%{public}s(%d) %{public}s[%p] boringssl_helper_create_certificate_buffer_chain_from_certificate_chain failed
chacha20 returned an unexpected value.
%{public}s(%d) MLKEM768_private_key not initialized
%{public}s(%d) ccgcm_set_iv failed
%{public}s(%d) %{public}s[%p] boringssl_helper_copy_public_key_from_certificates failed
%{public}s(%d) %{public}s[%p] Not resuming with recovered session state.
%{public}s(%d) %{public}s[%p] nw_protocol_supports_external_data(%s) is not valid
%{public}s(%d) PQ-TLS disabled; skipping fallback path
%{public}s(%d) %{public}s[%p] Already did cert lookup, continue
%{public}s(%d) %{public}s[%p] Warning [ATS FCPv2.1 violation]: Server certificate signed using signature algorithm %{public}s not advertised in client hello for server: %{public}s
%{public}s(%d) %{public}s[%p] boringssl_session_write called in state %{public}s (rdar://165275940)
began nw_protocol_boringssl_disconnect: boringssl session state is: %s
%{public}s(%d) %{public}s[%p] triggering input available
%{public}s(%d) %{public}s[%p] system_malloc(%u) failed
%{public}s(%d) %{public}s[%p] nw_frame_create_external failed
%{public}s(%d) %{public}s[%p] output buffer is NULL
%{public}s(%d) %{public}s[%p] SecTrustSetURLRequestAttribution(%lu) result: %d
%{public}s(%d) i2o_ECPublicKey failed
%{public}s(%d) %{public}s[%p] failed to get unclaimed bytes from batching frame
%{public}s(%d) %{public}s[%p] External data buffer length is too large. Partial writes are unsupported.
%{public}s(%d) %{public}s[%p] Already started the negotiation. Skipping.
%{public}s(%d) %{public}s[%p] not doing extra ATS trust eval for logging because logging redacted
%{public}s(%d) %{public}s[%p] Trust evaluation failed because of a NULL trust queue
%{public}s(%d) %{public}s[%p] Not setting invalid SNI value
%{public}s(%d) %{public}s[%p] Checking ATS trust evaluation for logging purposes
%{public}s(%d) %{public}s[%p] Using locally configured identity
%{public}s(%d) %{public}s[%p] Uncompressed data length exceeded buffer bounds
%{public}s(%d) %{public}s[%p] Certificate verification result: OK
%{public}s(%d) %{public}s[%p] SSL_set_chain_and_key failed: %d %s
%{public}s(%d) %{public}s[%p] Asyncing for session update block
%{public}s(%d) %{public}s[%p] get output frames min bytes %u max bytes %u
%{public}s(%d) %{public}s[%p] ignoring input_finished during pqtls fallback
%{public}s(%d) %{public}s[%p] ignoring disconnected during pqtls fallback
%{public}s(%d) %{public}s[%p] deflatInit failed
%{public}s(%d) %{public}s[%p] Failed to extract the SSL_SESSION bytes.
%{public}s(%d) %{public}s[%p] deflate failed
%{public}s(%d) %{public}s[%p] Asyncing for internal verify block
%{public}s(%d) %{public}s[%p] New session available
%{public}s(%d) %{public}s[%p] Using TLS 1.3 external PSK callback
%{public}s(%d) %{public}s[%p] TLS connected [server(%d) version(0x%04x) ciphersuite(%s) group(0x%04x) signature_alg(0x%04x) alpn(%{public}s) resumed(%d) offered_ticket(%d) in_early_data(%d) early_data_accepted(%d) false_started(%d) ocsp_rec
%{public}s(%d) %{public}s[%p] already in write frames, skipping
%{public}s(%d) evp_to_ccdigest_info(%d) failed
%{public}s(%d) %{public}s[%p] No PSK hint or selection logic. Using first PSK in the cache.
%{public}s(%d) %{public}s[%p] Error [ATS FCPv2.1 violation]: Server certificate signed using signature algorithm %{public}s not advertised in client hello for server: %{public}s
%{public}s(%d) %{public}s[%p] updating write secret. Level: %u, secret_data_length: %zu, currently negotiated ciphersuite: %u
%{public}s(%d) Unsupported EVP mode: %d
%{public}s(%d) %{public}s[%p] Failed to extract certificate #%zu
%{public}s(%d) %{public}s[%p] Error [ATS Violation]: ATS certificate trust requirement not satisfied for server: %{public}s
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: TLS version <1.2 negotiated for server: %{public}s
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: ECDSA key size %zu bits is less than minimum %d bits for server: %{public}s
%{public}s(%d) %{public}s[%p] CBB_add_bytes failed
%{public}s(%d) %{public}s[%p] allocated new batching frame: %u bytes capacity
%{public}s(%d) %{public}s[%p] boringssl_context_create_with_nw_context failed
%{public}s(%d) No support for cc digest with NID %i.
%{public}s(%d) %{public}s[%p] SecTrustSetOCSPResponse result: %d
%{public}s(%d) %{public}s[%p] SecTrustSetSignedCertificateTimestamps result: %d
%{public}s(%d) Failed to extract the private key from the leaf certificate
%{public}s(%d) %{public}s[%p] PSK lookup using identity hint did not find a match.
%{public}s(%d) %{public}s[%p] SSL_set_min_proto_version failed
%{public}s(%d) %{public}s[%p] calling SSL_shutdown.
%{public}s(%d) Clearning PSK identity
%{public}s(%d) %{public}s[%p] Connected in False Start.
%{public}s(%d) %{public}s[%p] Running TLS 1.3 external PSK client callback
%{public}s(%d) Initiating PQ-TLS fallback
%{sensitive}s
%{public}s(%d) %{public}s[%p] Returning from logging-only internal verify block with result: %{bool}d (%{public}@)
%{public}s(%d) %{public}s[%p] Warning [ATS Violation]: ATS certificate trust requirement not satisfied for server: %{public}s
%{public}s(%d) %{public}s[%p] authenticator validation failed
%{public}s(%d) %{public}s[%p] boringssl_bio_create failed
%{public}s(%d) %{public}s[%p] unable to copy context from parameters %p
%{public}s(%d) xpc_dictionary_create failed
%{public}s(%d) %{public}s[%p] Performing local trust evaluation
%{public}s(%d) %{public}s[%p] Incorrect type of ALPN protocol in list. Expected string or array, got %d
%{public}s(%d) %{public}s[%p] Failed to create queue %{public}s with QoS class %u.
%{public}s(%d) %{public}s[%p] boringssl_session_set_peer_verification_state_from_session failed
%{public}s(%d) Failed to allocate a boringssl_bio_state structure
%{public}s(%d) %{public}s[%p] input_available unacknowledged, data (%u bytes) over readahead threshold, suspending reads
%{public}s(%d) %{public}s[%p] Returned from client PSK selection callback %{public}s PSK.
%{public}s(%d) %{public}s[%p] Logging only trust evaluation failed because of a NULL trust queue
%{public}s(%d) %{public}s[%p] %{sensitive}s
poly1305 failed to be finalized.
%{public}s(%d) %{public}s[%p] %{public}s session cache hit
%{public}s(%d) RSA_PKCS1_OAEP_PADDING encryption not implemented
%{public}s(%d) ccgcm_update failed
%{public}s(%d) SSL_SESSION_to_bytes failed
%{public}s(%d) %{public}s[%p] SSL_set_signed_cert_timestamp_list failed
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: Leaf certificate hash algorithm (%d) is not at least SHA-256 for server: %{public}s
%{public}s(%d) %{public}s[%p] %{public}s handshake started
%{public}s(%d) %{public}s[%p] buffer is NULL and not peeking
%{public}s(%d) %{public}s[%p] TLS configured [server(%d) min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) c
%{public}s(%d) point2o_ECPublicKey failed
%{public}s(%d) %{public}s[%p] Returning from challenge block
%{public}s(%d) %{public}s[%p] Warning [ATS FCPv2.1 violation]: Signature algorithm rsa_pkcs15_sha1 negotiated by server: %{public}s
%{public}s(%d) No supported key exchange groups from the provided selection
%{public}s(%d) Clearning PSK data
%{public}s(%d) X9.62 serialization of an ECDH public key failed on calculating size.
%{public}s(%d) xpc_copy failed
%{public}s(%d) %{public}s[%p] %{public}s alert, level: %{public}s, description: %{public}s
%{public}s(%d) %{public}s[%p] Unexpected read result %d != %d
%{public}s(%d) %{public}s[%p] Failed to process input message
%{public}s(%d) %{public}s[%p] Waiting for output: %{public}s
%{public}s(%d) %{public}s[%p] Failed to set ECHconfig: %@
%{public}s(%d) ccec_verify failed
%{public}s(%d) %{public}s[%p] Returning from internal verify block with result: %{bool}d (%{public}@)
%{public}s(%d) %{public}s[%p] Asyncing for external verify block
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: Ciphersuite(%s) not offered in ATS negotiated for server: %{public}s
%{public}s(%d) boringssl_memory_malloc(%zu) failed
%{public}s(%d) %{public}s[%p] handshake failed at state %d: %s
%{public}s(%d) %{public}s[%p] Key usage requirement set to %d
%{public}s(%d) %{public}s[%p] data region %p, offset %zu
%{public}s(%d) %{public}s[%p] boringssl_context_set_identity failed
%{public}s(%d) %{public}s[%p] boringssl session state changed from %s to %s
%{public}s(%d) %{public}s[%p] nw_queue_context_create_source(timer) failed
%{public}s(%d) %{public}s[%p] Resuming reading frames
%{public}s(%d) %{public}s[%p] Already connected, reporting.
%{public}s(%d) %{public}s[%p] no remote endpoint
%{public}s(%d) Elliptic curve algorithm with NID %d is not supported
%{public}s(%d) %{public}s[%p] Asyncing for logging internal verify block
%{public}s(%d) %{public}s[%p] Invoking verify block
%{public}s(%d) %{public}s[%p] Cancelling TLS handshake timer
%{public}s(%d) %{public}s[%p] peeked %d bytes
%{public}s(%d) %{public}s[%p] Actually read %d bytes
%{public}s(%d) %{public}s[%p] SSL_get0_peer_certificates returned no certificates
%{public}s(%d) %{public}s[%p] Certificate signature alg: %d
%{public}s(%d) %{public}s[%p] SSL_set_strict_cipher_list failed
%{public}s(%d) %{public}s[%p] Passed max input threshold, stopping reading to deliver data (%u bytes)
%{public}s(%d) %{public}s[%p] nw_frame_create failed
%{public}s(%d) %{public}s[%p] boringssl_context_ssl_context_create failed
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: Leaf certificate is absent for server: %{public}s
%{public}s(%d) %{public}s[%p] Calling SSL_set_chain_and_key with %zu certificates
%{public}s(%d) 
%{public}s(%d) %{public}s[%p] EAP key material allocation failed
%{public}s(%d) %{public}s[%p] failed to finalize batching frame
%{public}s(%d) input protocol is NULL; skipping PQ-TLS fallback
%{public}s(%d) EVP_CIPH_CTR_MODE not implemented
%{public}s(%d) %{public}s[%p] Error [ATS violation]: Peer public key not set for server: %{public}s
chacha20 failed
%{public}s(%d) %{public}s[%p] incomplete write: %{public}s
%{public}s(%d) %{public}s[%p] SSL_SESSION_from_bytes failed
%{public}s(%d) %{public}s[%p] wrote %u bytes to batching frame
%{public}s(%d) %{public}s[%p] nw_protocol_connected_is_valid failed
%{public}s(%d) no parameters
%{public}s(%d) KYBER_public_key not initialized
%{public}s(%d) %{public}s[%p] Returning from external verify block with result: %{bool}d
%{public}s(%d) %{public}s[%p] Setting verify result to %{bool}d
%{public}s(%d) %{public}s[%p] no get_parameters callback
%{public}s(%d) %{public}s[%p] Creating larger frame to accommodate %u bytes
%{public}s(%d) SecKeyCreateSignature failed: %d
%{public}s(%d) %{public}s[%p] TLS handshake is complete using legacy TLS version
%{public}s(%d) %{public}s[%p] Client looking up PSK without server-provided hint
%{public}s(%d) Performing PQ-TLS fallback
%{public}s(%d) %{public}s[%p] nw_parameters_copy_context failed
%{public}s(%d) %{public}s[%p] PSK cache is empty.
%{public}s(%d) %{public}s[%p] No PSK selection logic. Indexing cache using identity hint verbatim.
%{public}s(%d) ccchacha20 failed
%{public}s(%d) %{public}s[%p] SSL_SESSION for resumption has ciphersuite: %s (id: %u)
%{public}s(%d) %{public}s[%p] Handshake incomplete: %{public}s [%d]
%{public}s(%d) PQ-TLS fallback disallowed for endpoint; skipping PQ-TLS fallback
%{public}s(%d) %{public}s[%p] no sec_protocol_options were supplied during instantiation
%{public}s(%d) %{public}s[%p] Lower protocol stack error post TLS handshake. [%d: %s]
%{public}s(%d) ECDSA_do_sign not implemented
%{public}s(%d) %{public}s[%p] Extended validation enforcement is enabled but the server certificate did not pass extended validation
%{public}s(%d) %{public}s[%p] Failed to create a SecTrust with the given certificates and policy
%{public}s(%d) %{public}s[%p] TLS 1.3 external PSK callback is not enabled
%{public}s(%d) %{public}s[%p] Failed to create trimmed frame
%{public}s(%d) %{public}s[%p] PQ-TLS fallback initiated; shortcircuiting the error propagation up the stack
%{public}s(%d) ecdsa_get_cc_curve_parameters(%d) failed
%{public}s(%d) %{public}s[%p] SSL_get0_signed_cert_timestamp_list returned no SCT extension data
%{public}s(%d) %{public}s[%p] Error [ATS violation]: Leaf certificate is absent for server: %{public}s
%{public}s(%d) BIO_new(BIO_nw_protocol()) failed
%{public}s(%d) %{public}s[%p] get input frames expected min bytes %u expected max bytes %u
%{public}s(%d) safe input protocol is NULL; skipping PQ-TLS fallback
%{public}s(%d) ccgcm_finalize failed
%{public}s(%d) The leaf of the certificate chain is not a SecIdentityRef
%{public}s(%d) %{public}s[%p] Error [ATS violation]: RSA key size %zu bits is less than minimum %d bits for server: %{public}s
%{public}s(%d) KYBER_private_key not initialized
%{public}s(%d) Cannot build serialized session state: %d + %zu > %zu
%{public}s(%d) %{public}s[%p] No certificates present in the list
%{public}s(%d) %{public}s[%p] SecTrustCreateWithCertificates result: %d
%{public}s(%d) %{public}s[%p] TLS handshake is complete using TLS 1.3 version
%{public}s(%d) %{public}s[%p] Handshake took more than %d seconds to complete, closing this session
%{public}s(%d) %{public}s[%p] no parameters
%{public}s(%d) %{public}s[%p] Returning %u frames (%u bytes) to input handler
Restricted mode: Returning restricted default ciphersuite set.
%{public}s(%d) %{public}s[%p] Restarting handshake
%{public}s(%d) %{public}s[%p] read request: %u
%{public}s(%d) %{public}s[%p] no input frames available
%{public}s(%d) %{public}s[%p] failed to claim %d bytes from %p
%{public}s(%d) %{public}s[%p] Signaling premature connect in early data mode
%{public}s(%d) %{public}s[%p] boringssl_context_ssl_context_create_datagram failed
%{public}s(%d) %{public}s[%p] No TLS-provided SCTs
%{public}s(%d) RSA_NO_PADDING encryption not implemented
%{public}s(%d) EC_POINT_point2oct failed: got %i, expected >0
%{public}s(%d) %{public}s[%p] boringssl_memory_malloc(%zu) failed
%{public}s(%d) %{public}s[%p] Reusing context
%{public}s(%d) %{public}s[%p] Error: %{private}s
%{public}s(%d) cckem_decapsulate failed
%{public}s(%d) %{public}s[%p] Cannot get any bytes in current state
%{public}s(%d) %{public}s[%p] get output frames failed, state %d
%{public}s(%d) boringssl session create failed
%{public}s(%d) RSA_sign_raw not implemented
%{public}s(%d) ccec_verify_composite failed
%{public}s(%d) %{public}s[%p] SSL_set1_curves failed
%{public}s(%d) %{public}s[%p] Received incorrectly encoded SerializedSCT list
%{public}s(%d) %{public}s[%p] Client using server-provided identity hint for PSK lookup
%{public}s(%d) %{public}s[%p] No PSK found in client cache
%{public}s(%d) BoringSSL %p: %{public}s
%{public}s(%d) %{public}s[%p] read error code %d
%{public}s(%d) %{public}s[%p] SSL_set_ocsp_response failed
%{public}s(%d) %{public}s[%p] Applying EV constraint
%{public}s(%d) %{public}s[%p] encryption_write_level %u -> %u
%{public}s(%d) %{public}s[%p] SSL_set_quic_method failed
%{public}s(%d) %{public}s[%p] In early data: %{public}s
%{public}s(%d) %{public}s[%p] %{public}s
%{public}s(%d) %{public}s[%p] boringssl_session_apply_protocol_options_for_transport failed
%{public}s(%d) %{public}s[%p] Serialized data is not of the correct content type.
%{public}s(%d) %{public}s[%p] Incorrect type of ALPN protocol in list. Expected array of length 2, got %zu
%{public}s(%d) %{public}s[%p] Cached context state is invalid.
%{public}s(%d) %{public}s[%p] Failed to copy PSK hint data
%{public}s(%d) The type of the leaf certificate is not that of `SecIdentityGetTypeID()`
%{public}s(%d) ccec_import_pub failed: got %i, expected 0
%{public}s(%d) %{public}s[%p] Generating ATS violation error
%{public}s(%d) %{public}s[%p] Incorrect uncompressed length. Expected %zu, got %zu
%{public}s(%d) %{public}s[%p] %{public}s handshake done
%{public}s(%d) %{public}s[%p] Unhandled %{public}s alert level: %d
%{public}s(%d) %{public}s[%p] Installing session cache state
%{public}s(%d) %{public}s[%p] SSL_set_tlsext_host_name failed
%{public}s(%d) %{public}s[%p] encryption_read_level %u -> %u
%{public}s(%d) %{public}s[%p] nw_frame_create failed for %d bytes
%{public}s(%d) %{public}s[%p] SSL_set_quic_transport_params failed
%{public}s(%d) %{public}s[%p] Unsupported sec_identity provided (%d)
%{public}s(%d) %{public}s[%p] boringssl_helper_create_CRYPTO_BUFFER_list_from_stack failed
%{public}s(%d) %{public}s[%p] %{public}s %{public}s %zu bytes
%{public}s(%d) %{public}s[%p] Error [ATS FCPv2.1 violation]: TLS 1.2 negotiated without extended master secret (EMS) for server: %{public}s
%{public}s(%d) %{public}s[%p] nw_protocol_get_output_frames(%s) is not valid
%{public}s(%d) %{public}s[%p] set %{public}d
poly1305 failed to be initialized.
%{public}s(%d) no parameters; skipping PQ-TLS fallback
%{public}s(%d) %{public}s[%p] Error not propagated up the stack
%{public}s(%d) %{public}s[%p] inflateInit failed
%{public}s(%d) CFArrayCreateMutable failed
%{public}s(%d) Failed to allocate a boringssl context state object.
%{public}s(%d) %{public}s[%p] Asyncing for challenge block
%{public}s(%d) %{public}s[%p] Connection is ATS compliant
%{public}s(%d) %{public}s[%p] read request: %u byte(s)
%{public}s(%d) %{public}s[%p] bytes read: %u
%{public}s(%d) %{public}s[%p] No TLS-provided OCSP response
%{public}s(%d) Failed to extract the certificate from the leaf (first element of the certificate chain)
%{public}s(%d) %{public}s[%p] set %{public}s
%{public}s(%d) %{public}s[%p] EV constraint passed
%{public}s(%d) %{public}s[%p] Error [ATS violation]: ECDSA key size %zu bits is less than minimum %d bits for server: %{public}s
%{public}s(%d) %{public}s[%p] session state: %s [%d]
%{public}s(%d) no remote endpoint; skipping PQ-TLS fallback
%{public}s(%d) MLKEM768_public_key not initialized
%{public}s(%d) get_cp_for_pub_size failed
%{public}s(%d) %{public}s[%p] set %{public}zu
%{public}s(%d) %{public}s[%p] Not resuming session to a different address if EMS was not negotiated.
%{public}s(%d) %{public}s[%p] %{public}s session cache miss
%{public}s(%d) %{public}s[%p] No PSK found in server cache
%{public}s(%d) RSA_sign not implemented
%{public}s(%d) %{public}s[%p] Requiring client cert
%{public}s(%d) %{public}s[%p] SerializedSCT length %d
%{public}s(%d) %{public}s[%p] Invalid sec_identity provided (SEC_PROTOCOL_IDENTITY_TYPE_INVALID)
%{public}s(%d) %{public}s[%p] ECH is %s
%{public}s(%d) %{public}s[%p] boringssl_helper_zlib_decompress_data failed
%{public}s(%d) %{public}s[%p] Certificate verification result: FAIL
%{public}s(%d) %{public}s[%p] currently in early data? %s, early data accepted? %s
%{public}s(%d) %{public}s[%p] SSL_set1_ech_config_list failed
%{public}s(%d) %{public}s[%p] no output handler available
%{public}s(%d) %{public}s[%p] TLS context is NULL. The connection was likely torn down between add_input_handler and connected callbacks.
%{public}s(%d) boringssl session set bio failed
%{public}s(%d) boringssl_memory_malloc failed
%{public}s(%d) Cannot build serialized session state: %d + %zu + %zu + %zu > %zu
%{public}s(%d) %{public}s[%p] Ignoring ALPN, no valid protocols
%{public}s(%d) %{public}s[%p] Subject name: %{public}s, tls_handshake_trust: %{bool}d
%{public}s(%d) CFDataCreateMutable failed
%{public}s(%d) %{public}s[%p] flushed batching frame: %s
%{public}s(%d) %{public}s[%p] received output available
%{public}s(%d) %{public}s[%p] Not enough bytes in record to satisfy request (%u < %u)
%{public}s(%d) rsa_default_sign_raw not implemented
%{public}s(%d) %{public}s[%p] Skipping local ATS trust evaluation (ats_trust_policy=skip)
%{public}s(%d) %{public}s[%p] Cancelled during verify block
%{public}s(%d) %{public}s[%p] ALPN protocol exceeds length restrictions (%zu): %{public}s
%{public}s(%d) %{public}s[%p] 
%{public}s(%d) %{public}s[%p] failed to unclaim %d bytes from %p
%{public}s(%d) %{public}s[%p] Success setting ECHconfig
%{public}s(%d) RSA_padding_add_PKCS1_OAEP_mgf1 not implemented
%{public}s(%d) Failed to log metrics
%{public}s(%d) %{public}s[%p] CFDataCreate failed
%{public}s(%d) %{public}s[%p] Cancelled during challenge block
%{public}s(%d) %{public}s[%p] Incorrect type of ALPN protocol in list. Expected array with a string
%{public}s(%d) %{public}s[%p] Session state %{public}s.
%{public}s(%d) %{public}s[%p] ats_ciphersuites unexpectedly NULL
%{public}s(%d) %{public}s[%p] Error [ATS violation]: Leaf certificate hash algorithm (%d) is not at least SHA-256 for server: %{public}s
%{public}s(%d) %{public}s[%p] Skipping content type %d
boringssl called disconnect down the stack
%{public}s(%d) %{public}s[%p] first frame cannot be larger than the frame array
%{public}s(%d) %{public}s[%p] Failed to flatten external data %@ (offset %u, unclaimed %u)
%{public}s(%d) %{public}s[%p] CFArrayCreateMutable failed
%{public}s(%d) ccec_import_pub failed
%{public}s(%d) %{public}s[%p] SecTrustEvaluateAsyncWithError failed
%{public}s(%d) %{public}s[%p] Performing external trust evaluation
%{public}s(%d) %{public}s[%p] fcs_v2_ciphersuites unexpectedly NULL
%{public}s(%d) %{public}s[%p] Cached session state is invalid.
%{public}s(%d) %{public}s[%p] Cannot copy frame, bad offset (%u >= %u)
%{public}s(%d) %{public}s[%p] Propagating error up the stack
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: RSA key size %zu bits is less than minimum %d bits for server: %{public}s
%{public}s(%d) %{public}s[%p] Failed to set the %u QoS class attribute for queue %{public}s.
%{public}s(%d) %{public}s[%p] %{public}s handshake state: %{public}s
%{public}s(%d) %{public}s[%p] Returning from session update block
%{public}s(%d) %{public}s[%p] Rebuilding session state for resumed session
%{public}s(%d) CFStringGetCString failed
%{public}s(%d) %{public}s[%p] Frame with wake flag detected
%{public}s(%d) %{public}s[%p] old input handler does not match (%p != %p)
%{public}s(%d) BN_bn2bin_padded failed
%{public}s(%d) %{public}s[%p] Restricted mode: Provided minimum version (0x%x) was capped to (0x%x).
%{public}s(%d) %{public}s[%p] Calling SSL_set_private_key_method
%{public}s(%d) %{public}s[%p] %{public}s session state %{public}s.
%{public}s(%d) %{public}s[%p] Warning [ATS violation]: Peer public key not set for server: %{public}s
%{public}s(%d) Failed to get boringssl cipher for ciphersuite 0x%04x
%{public}s(%d) %{public}s[%p] state: %d, ignore handshake negotiate
%{public}s(%d) %{public}s[%p] Set peer trust data
%{public}s(%d) %{public}s[%p] Failed to set peer trust data
%{public}s(%d) %{public}s[%p] received add input handler again
%{public}s(%d) %{public}s[%p] Warning [ATS FCPv2.1 violation]: Ciphersuite(%s) not offered in ATS FCP_v2.1 mode negotiated for server: %{public}s
%{public}s(%d) %{public}s[%p] Wrote decompressed certificate data
%{public}s(%d) %{public}s[%p] Unable to extract cached certificates from the SSL_SESSION object
%{public}s(%d) %{public}s[%p] write request: %u
%{public}s(%d) %{public}s[%p] Above maximum input threshold, skipping read and resuspending (%u bytes)
%{public}s(%d) cckem_encapsulate failed
%{public}s(%d) %{public}s[%p] Invoking SecTrustEvaluateAsyncWithError
calc_tag failed
%{public}s(%d) %{public}s[%p] claiming batching frame with %u bytes failed
%{public}s(%d) %{public}s[%p] cannot peek into the session
%{public}s(%d) Failed to get signature algorithm: %{public}d
%{public}s(%d) ECDSA_sign not implemented
%{public}s(%d) %{public}s[%p] New context
%{public}s(%d) Input array is NULL
%{public}s(%d) Input array length is 0 (empty)
%{public}s(%d) %{public}s[%p] current input frame (%p) does not match frame being processed (%p)
%{public}s(%d) %{public}s[%p] Signaling premature connect due to False Start
%{public}s(%d) %{public}s[%p] unable to write frame array of length %u and pending buffer %u
%{public}s(%d) RSA_padding_check_PKCS1_OAEP_mgf1 not implemented
%{public}s(%d) %{public}s[%p] %4lu   %s   %s
%{public}s(%d) %{public}s[%p] Not requesting client cert
%{public}s(%d) %{public}s[%p] not doing extra ATS trust eval for logging because real ATS is happening
%{public}s(%d) %{public}s[%p] not doing extra ATS trust eval because process is not non-Safari/WebKit or third party
%{public}s(%d) %{public}s[%p] waiting for writable frames
%{public}s(%d) %{public}s[%p] ignoring error during pqtls fallback
%{public}s(%d) Cannot build serialized session state: %d + %zu + %zu > %zu
%{public}s(%d) %{public}s[%p] SSL_set_max_proto_version failed
%{public}s(%d) %{public}s[%p] Wrote compressed certificate data
%{public}s(%d) No supported ciphersuites from the provided selection
%{public}s(%d) %{public}s[%p] relaying output available log
%{public}s(%d) no TLS options; skipping PQ-TLS fallback
%{public}s(%d) %{public}s[%p] Lower protocol stack error pre TLS handshake. [%d: %s]
%{public}s(%d) ccgcm_reset failed
%{public}s(%d) %{public}s[%p] Warning [ATS FCPv2.1 violation]: TLS 1.2 negotiated without extended master secret (EMS) for server: %{public}s
%{public}s(%d) %{public}s[%p] total bytes written: %u
%{public}s(%d) %{public}s[%p] Failed to allocate %d bytes for input_buffer from buffer manager
%{public}s(%d) ccgcm_aad failed
%{public}s(%d) %{public}s[%p] Will request optional client cert
chachapoly tag calculation failed.
boringssl_concrete_boringssl_psk
OS_boringssl_context_state
NSObject
OS_boringssl_session_cache
boringssl_concrete_boringssl_session_state
boringssl_concrete_boringssl_identity
boringssl_concrete_nw_protocol_boringssl
boringssl_concrete_boringssl_session_cache
OS_boringssl_session_state
boringssl_concrete_boringssl_context_state
boringssl_concrete_boringssl_psk_cache
OS_nw_protocol_boringssl
OS_boringssl_psk
OS_boringssl_identity
OS_boringssl_psk_cache
boringssl_concrete_boringssl_ctx
OS_boringssl_ctx
description
grease_enabled
peer_trust_ref
ssl_max_version
log_identities_redacted
new_session_ticket_request
ssl_state
context
encryption_write_level
legacy_ats_applicable
metadata
output_handshake_frame_array
response_epoch_ms
self
servicing_reads
alpn_enabled
connected_callback
old_ats_enforced
fallback_mode
subject_name
handshake_end
offered_ticket
certificate_compression_used
verify_queue
debugDescription
ech_enabled
old_identity
pqtls_enabled
allow_server_identity_change
connection_id
early_output_handler
isMemberOfClass:
pending_output_buffer_length
remote_address
resumed_session_ticket_request
handshake_timer
outbound_byte_count
pqtls_fallback_initiated
ats_non_pfs_ciphersuite_allowed
output_application_frame_array
received_certificate_request
ats_violation_detected
key
pake_offered
early_data_enabled
handshake_start
boringssl_handle
alert_callback
ssl_ctx
write_func
log_str
current_handshake_type
message_mode
association
peer_cert_chain
async_count
callbacks
hash
private_key_decrypt_block
session_update_block
zone
key_update_block
sct_enable
message_writer
output_protocol_supports_early_data
autorelease
class
handshake_func
hasSuffix:
trust_evaluation_complete
conformsToProtocol:
handshake_message_callback
legacy_context
parameters
stack_error
TQ,R
input_suspended
certificate_compression_algorithm
connected
private_key_queue
write_ready
fcs_tls_v2_compliance_mode_enabled
output_batched_bytes_written
internal_error
isEqual:
received_connect
async_context
peer_public_key
finalized_output_frame_array
output_initial_frame_array
performSelector:
tls13_chacha20poly1305_enabled
address_string
flight_direction
recovered_session
server_raw_public_key_certificates
session_state
tried_resumption
ssl_min_version
handshake_message_callback_queue
output_early_frame_array
peer_trust_result
total_flight_time
decrypt_block
is_local_networking
peer_verified
psk_negotiated
isProxy
ref_cnt
cancelled
.cxx_destruct
private_key
inbound_byte_count
output_pending_length
session_update_queue
skip_ats_trust_evaluation
ats_enforced
dtls
handshake_state_callback
performSelector:withObject:withObject:
started_flight
ats_failure_reason
read_frame_array
renewed
external_frames
ats_applicable
handshake_output_handler
deferred_input_finished
input_available_unacknowledged
is_probe
private_key_operation_complete
respondsToSelector:
used_extended_master_secret
superclass
dataWithBytes:length:
certificate_signature_algorithm
certificates
isKindOfClass:
psk_cache
sent_error
options
release
decryption_result
servicing_handshake
trust_invalid_certs
write_stalls
in_write_frames
cached_content_type
current_flight_time
did_receive_data_once
read_ready
started_negotiation
verify_block
certificate_compression_enabled
input_frame_byte_count
npn_enabled
peer_trust_evaluation_error
private_key_sign_block
boringssl_bio
experiment_identifier
serialized_session
ssl_alert
minimum_ecdsa_key_size
minimum_rsa_key_size
performSelector:withObject:
session_ticket_enabled
tls13_aesgcm_enabled
tls13_epsk_offered
internal_reference
old_ats_enforced_compat
output_frame_array
server
stringWithUTF8String:
challenge_queue
backup_peer_trust_ref
minimum_signature_algorithm
pending_output_buffer
initWithPSK:::::
retain
signature_result
ssl_session
T#,R
alpn_protocols
challenge_block
pending_output_data
psk_selection_block
sign_block
false_start_enabled
wake_flag
identity
session_cache
application_output_handler
current_input_frame
key_update_queue
read_stalls
T@\"NSString\",R,C
logging_disabled
psk_selection_queue
unassigned_input_frame_array
waiting_for_writable
client_raw_public_key_certificates
handshake_timer_fires
list
nsURLRequestAttribution
T@\"NSString\",?,R,C
enforce_ev
queue
read_func
serialized_session_length
cert_lookup_done
containsString:
claimed_input_bytes
current_handshake_state
input_frame_array
ocsp_enable
destroy
encryption_read_level
output_batching_frame
resumed
false_start_used
peer_verification_in_progress
dealloc
initial_output_handler
request_epoch_ms
retainCount
ciphersuite_configuration_string
^?
@\"boringssl_concrete_boringssl_ctx\"
@\"boringssl_concrete_boringssl_session_cache\"
@32@0:8:16@24
B16@0:8
@\"NSObject<OS_dispatch_queue>\"
B
{boringssl_ctx_alert=\"ssl_alert_type\"i\"ssl_alert_level\"C\"ssl_alert_code\"C\"ssl_warning_count\"C}
Q16@0:8
^{_NSZone=}16@0:8
@\"NSObject<OS_nw_frame>\"
@\"NSObject<OS_nw_parameters>\"
^{__CFArray=}
[84c]
@16@0:8
@40@0:8:16@24@32
B24@0:8@16
^v
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
@\"boringssl_concrete_nw_protocol_boringssl\"
^{__SecTrust=}
Vv16@0:8
I
{nw_frame_array_s=\"tqh_first\"^{nw_frame}\"tqh_last\"^^{nw_frame}}
^{ssl_ctx_st=}
C
S
@\"boringssl_concrete_boringssl_identity\"
^{ssl_st=}
@\"NSObject<OS_nw_protocol_options>\"
@?
^{boringssl_legacy_ctx=I^v}
@\"NSObject<OS_xpc_object>\"
@\"NSObject<OS_nw_association>\"
Q
@\"NSObject<OS_sec_array>\"
^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v}
r*
B24@0:8#16
r^v
b1
(sockaddr_in_4_6=\"sa\"{sockaddr=\"sa_len\"C\"sa_family\"C\"sa_data\"[14c]}\"sin\"{sockaddr_in=\"sin_len\"C\"sin_family\"C\"sin_port\"S\"sin_addr\"{in_addr=\"s_addr\"I}\"sin_zero\"[8c]}\"sin6\"{sockaddr_in6=\"sin6_len\"C\"sin6_family\"C\"si
*
@\"NSObject<OS_sec_identity>\"
B24@0:8:16
v16@0:8
i
[16C]
@\"NSObject<OS_nw_protocol_metadata>\"
@\"NSString\"16@0:8
@\"NSObject<OS_dispatch_data>\"
@\"NSObject<OS_nw_context>\"
@\"boringssl_concrete_boringssl_psk_cache\"
@\"boringssl_concrete_boringssl_session_state\"
#16@0:8
@\"NSObject<OS_nw_array>\"
@24@0:8:16
B24@0:8@\"Protocol\"16
illegal parameter
user canceled
emailAddress
setct-ErrorTBS
AES-256-CFB8
div.c.inc
boringssl_metrics_create_ech_event
id-smime-aa-contentIdentifier
id-regCtrl-regToken
hs->ssl->s3->write_level == ssl_encryption_initial
ECDSA_do_verify
sha1WithRSA
Invalidity Date
member
boringssl_context_set_encryption_secrets
fe_mul121666
ECDHE-RSA-AES128-GCM-SHA256
boringssl_bio_destroy
wvalue < (1u << window)
FILE pointer
has_ecdhe_group
close notify
tls13_server.cc
com.waze.iphone
waiting to look up Channel ID key
outgoing_byte_count
!(outer_tag & CBS_ASN1_CONSTRUCTED)
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/bytestring/cbb.c
chacha.c
B24@?0Q8@\"NSObject<OS_xpc_object>\"16
out->pctx == NULL || out->pctx_ops != NULL
com.quark.browser
resumption_attempted
DES-EDE3-CFB
set-ctype
sect283k1
GOST R 34.11-94 with GOST R 34.10-2001
com.poshmark.poshmark
ssl_client_hello_decrypt
PEM routines
Microsoft Extension Request
OCSPSigning
id-pkix1-explicit-93
type != ssl_client_hello_outer
handle_hello_verify_request
!session
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc
com.thehomedepot.homedepot
n0 < d0
boringssl_context_state_create
CBB_discard_child
c2tnb191v2
!buffers_alias(out, in_len, in, in_len) || in == out
DES-EDE3-CBC
com.disney.disneyplus
extReq
id-smime-alg
ECDHE-ECDSA-AES128-GCM-SHA256
!BN_is_negative(&mont->N)
in.size() >= SSL3_RT_HEADER_LENGTH
Netscape Revocation Url
subjectInfoAccess
wap-wsg-idm-ecid-wtls3
true
id-mod-timestamp-protocol
psk_used
common libcrypto routines
des-ede3-cbc
pbeWithSHA1And3-KeyTripleDES-CBC
dhSinglePass-cofactorDH-sha384kdf-scheme
hpke.c
desc != SSL_AD_CLOSE_NOTIFY
certificate lookup pending
id-mod-cmp
biometricInfo
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m
disabled
boringssl_session_install_association_state
BIO routines
id-mod-qualified-cert-93
IPSec Tunnel
X509v3 No Revocation Available
mailPreferenceOption
should_offer_early_data
!SSL_in_init(ssl)
DTLSv1.2
mul.c.inc
aes_nohw_from_batch
id-smime-mod-ets-eSigPolicy-97
id-smime-aa-ets-revocationValues
role
setct-CertReqTBE
com.epic.mychart
disconnected
Hold Instruction None
setAttr-TokenType
brainpoolP160r1
1 `
do_reverify_server_certificate
digest_update
ec_GFp_nistp256_cmp_x_coordinate
setct-AuthRevResBaggage
dhSinglePass-cofactorDH-sha1kdf-scheme
boringssl_context_restore_ssl_context
TLS_RSA_WITH_3DES_EDE_CBC_SHA
ECDHE
TLS 1.3 server send_server_finished
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc
tls1_record_handshake_hashes_for_channel_id
com.nextdoor.nextdoor
initials
X500algorithms
aes-192-ecb
secp112r2
nw_protocol_error_print
ssl->d1->outgoing_written < ssl->d1->outgoing_messages.size()
padding.c.inc
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc
com.airbnb.app
RSA-PKCS1v15-SHA256
SHOULD_NOT_HAVE_BEEN_CALLED
BF-CFB
BN_is_odd(&mont->N)
com.alibaba.iAliexpress
get_cp_for_pub_size
setct-CredRevReqTBE
wap-wsg-idm-ecid-wtls8
rsassaPss
SSL3_RT_HANDSHAKE
boringssl_context_new_session_handler
sha256.c.inc
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc
ext_ri_add_serverhello
0 <= tna && tna < n
com.baidu.netdisk
camellia-192-cbc
cryptopro
RSA_sign_raw
com.parentsquare.psapp
deltaRevocationList
constant_time_declassify_int(f->v[_assert_fe_i] <= (0x8ccccccccccccULL))
BN_STACK_pop
boringssl_metrics_log_metric_with_bundle_identifier
X509v3 Issuer Alternative Name
id-mod-cmp2000
unknown
serialNumber
Authority Information Access
holdInstructionCallIssuer
caRepository
Any Extended Key Usage
do_cert_callback
TLS_PSK_WITH_AES_256_GCM_SHA384
!ssl->s3->has_message
com.ebay.iphone
wnaf.c.inc
Time Stamping
id-smime-aa-encapContentType
camellia-256-cfb8
AES-256-CBC-HMAC-SHA1
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc
not completed
is_local_networking
nsCaPolicyUrl
setct-PANOnly
CAMELLIA-192-CFB
dsa_with_SHA224
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_aead_ctx.cc
USER
mgf1
com.xiaojukeji.didi
com.gauthmath.intelligence
stack.c
GOST 28147-89 Cryptocom ParamSet
v16@?0@\"NSObject<OS_sec_identity>\"8
TLS server verify_client_certificate
tls13_add_certificate_verify_in_buffer
ssl_add_clienthello_tlsext_inner
com.taobao.taobao4iphone
.apple
RC5-CBC
private
secp128r1
boringssl_context_set_ats_applicable
ext_quic_transport_params_parse_clienthello_impl
com.tencent.live4iphone
com.affirm.recharge
cbb->u.child.offset + cbb->u.child.pending_len_len <= cbb->u.child.base->len
RSA-SHA1-2
id-cct-PKIResponse
setct-CertReqTBEX
physicalDeliveryOfficeName
valid
ipsec3
AuthRSA
BN_bin2bn
SSL_CIPHER_get_bits
sha384WithRSAEncryption
SSL library error
RC2-CBC
ppBasis
c2pnb163v3
secp128r2
id-Gost28147-89-CryptoPro-Oscar-1-1-ParamSet
GOST R 34.11-94 with GOST R 34.10-94 Cryptocom
com.microsoft.Office.Outlook
com.360buy.jdmobile
Generate
id-GostR3410-94DH
boringssl_context_set_ats_minimum_ecdsa_key_size
TLS_ECDH_RSA_WITH_AES_128_CBC_SHA
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/bio/bio.c
CBS_len(&extensions) == 0
Netscape Data Type
OCSP Signing
DES-EDE3-CFB1
CAMELLIA-256-CFB8
engine.c
ec_GFp_nistp224_point_mul_public
bn_fits_in_words(bn, width)
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/p_x25519.c
id-aca-authenticationInfo
OCSP Nonce
AES-192-OFB
additional verification
sect409r1
exponentiation.c.inc
protocol.size() < UINT_MAX
constant_time_declassify_int(h->v[_assert_fe_i] <= (0x8ccccccccccccULL))
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_cipher.cc
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/evp_asn1.c
com.amazon.AmazonJP
id-aca-chargingIdentity
dcObject
hs->credential != nullptr
boringssl_memory_copy_array
fallback_attempted
secretary
ssl->session == nullptr
SSL_CIPHER_get_kx_nid
!hs->can_release_private_key
montgomery_inv.c.inc
com.amazon.Lassen
com.microsoft.msedge
boringssl_helper_dump_dispatch_data_block_invoke
out_ber_found == NULL
setct-RegFormResTBS
3 `
nw_protocol_boringssl_reset
CBB_flush
CAMELLIA-192-CBC
id-GostR3410-94-CryptoPro-A-ParamSet
0`
aead_tls_open
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc
TLS 1.3 client unknown
(SSL_get_options(hs->ssl) & SSL_OP_NO_TICKET) == 0
com.magmic.NYTCrosswords09
handoff error
BN_div
com.amazon.AmazonUK
bn_reduce_once_in_place
setct-AuthTokenTBE
setct-CredResTBE
auth-psk
co_list[num - 1].cipher != nullptr
DES-CBC3-SHA
TLS_PSK_WITH_AES_128_CBC_SHA
nw_protocol_boringssl_add_input_handler
tls_on_handshake_complete
TLS 1.3 client read_certificate_request
com.mcdonalds.gma
com.instacart
CAST5-OFB
JOINT-ISO-ITU-T
owner
tls_seal_scatter_prefix_len(ssl, type, in_len) == split_record_len + SSL3_RT_HEADER_LENGTH - 1
com.intsig.CamScannerLite
des-ede3-cfb
id-ce
rc2-40-cbc
aes-128-cbc
fe_carry
ECDHE-ECDSA-AES256-SHA
TLS 1.3 server select_parameters
com.booking.BookingApp
boringssl_helper_copy_leaf_certificate_from_chain
tls_version
nsCertSequence
documentTitle
SSL3_RT_APPLICATION_DATA
EVP_AEAD_CTX_open
org.whispersystems.signal
kdf_id == EVP_HPKE_HKDF_SHA256
Strong Extranet ID
camellia-192-cfb
businessCategory
com.sina.weibo
byte_count
cert_signature_algorithm
setct-CapResTBE
TLS_PSK_WITH_AES_128_CBC_SHA256
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/ex_data.c
v16@?0@\"boringssl_concrete_nw_protocol_boringssl\"8
false
nw_protocol_boringssl_write_to_batching_frame
in.size() <= SSL3_RT_MAX_PLAIN_LENGTH
legacy_ats_pfs
rFC822localPart
setct-AuthRevReqBaggage
setct-PI-TBS
setCext-cCertRequired
set-brand-MasterCard
Any language
fe_add
aRSA
!result || written_suffix_len == suffix_len
rb
cbs_convert_ber
X9-57
sha512-256
len == 0
digest_len == hs->new_session->original_handshake_hash.size()
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/dsa/dsa_asn1.c
HMAC routines
cbs.c
boringssl_context_set_ocsp_response
boringssl_context_evaluate_trust_async_external_block_invoke_3
PSK-AES128-CBC-SHA
certificate unknown
com.google.Classroom
id-ecPublicKey
 `
constant_time_declassify_int(borrow <= 1)
ssl_send_alert_impl
ConfigurableSecurityPolicyRestrictTLS
pbeWithSHA1AndDES-CBC
fe_sq_tt
.
com.kuaishou.nebula
com.youku.YouKu
TLS client send_client_key_exchange
METHOD_ref
com.espn.ScoreCenter
no error
OCSP CRL ID
homePostalAddress
setct-PResData
sect409k1
HMAC GOST 34.11-94
gost89
do_send_client_certificate_verify
DC
setct-AuthRevResData
TLS client read_session_ticket
ssl_check_leaf_certificate
RSA-NP-MD5
Oakley-EC2N-4
CAMELLIA-256-OFB
boringssl_context_certificate_request_callback_block_invoke_3
unknown PSK identity
TLS 1.3 server unknown
function should not have been called
pkcs7-data
constant_time_declassify_int(fits_in_bytes(in, in_len, out_len))
SSL_get_ciphers
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/t1_enc.cc
ssl_handle_open_record
connection established
mac_secret_length <= sizeof(hmac_pad)
dnQualifier
boringssl_context_set_ats_minimum_rsa_key_size
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
SHA512
pool.c
hs->ssl->quic_method != nullptr
DIGEST_LIB
Netscape Renewal Url
pkcs8ShroudedKeyBag
CSPName
secp160r1
key->pub_key == NULL
sha256_final_impl
ext_quic_transport_params_parse_serverhello_impl
com.unionpay.chsp
RAND_LIB
id-aca-role
id-GostR3410-94-CryptoPro-XchC-ParamSet
X25519
unknown state
ECDSA-X962-SHA1
OCSP No Check
boringssl_session_apply_protocol_options_for_transport_block_invoke
malloc failure
child->base == base
TLS Web Client Authentication
set-brand-Diners
boringssl_context_log_potential_ats_violation_peer_public_key_size
TLS_RSA_WITH_AES_128_GCM_SHA256
dtls1_is_current_message_complete(ssl)
fopen('
com.cvs.cvspharmacy
cbb_add_child
sect571r1
telexNumber
md_len % 4 == 0
cNAMERecord
x121Address
com.blockpuzzle.us.ios
wap-wsg-idm-ecid-wtls9
cACertificate
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
boringssl_session_apply_protocol_options_for_transport_block_invoke_2
tls1_get_shared_group
nsSGC
setAttr-PGWYcap
TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA
TLS 1.3 client read_server_hello
process
MDC2
id-smime-mod-ess
setCext-Track2Data
hs->config->signed_cert_timestamps_enabled
com.burbn.barcelona
PEM
DIGEST
GOST R 34.11-94 with GOST R 34.10-94
SHA384
no application protocol
bn_mod_exp_mont_small
X509V3_LIB
authorityKeyIdentifier
ssl_session_protocol_version
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA
com.apple.boringssl
nw_boringssl_read
div_extra.c.inc
com.microsoft.azureauthenticator
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc
ASN.1 encoding routines
NIST P-256
sha
CBB_finish_i2d
data_plus_mac_len >= HMAC_size(&tls_ctx->hmac_ctx)
id-smime-ct-TDTInfo
X509v3 Policy Constraints
ANSI X9.62
setCext-hashedRoot
dhSinglePass-cofactorDH-sha512kdf-scheme
TLS client enter_early_data
SSL_CONFIG
encrypted track 2
postOfficeBox
ssl->s3->version == 0 || (hs->early_data_offered && ssl->s3->version == hs->early_session->ssl_version)
nw_protocol_boringssl_flush_batching_frame
TLSv1.3
SSL_set_shutdown
ticket_offered
serverAuth
id-cmc-identification
c2onb239v4
X509v3 Any Policy
ext_alps_parse_serverhello_impl
com.fidelity.watchlist
ASN1_LIB
description
manager
id-GostR3410-2001DH
authorityRevocationList
dh-cofactor-kdf
EVP_DecryptFinal_ex
com.kouzoh.ios.mercari
countryName
shaWithRSAEncryption
aes-192-cbc-hmac-sha1
do_read_server_hello
net.whatsapp.WhatsApp
PKCS7_LIB
PBKDF2
id-cmc-statusInfo
AES-192-CFB8
userCertificate
((struct openssl_method_common_st*) method_in)->is_static
!hs->config->alpn_client_proto_list.empty()
com.burbn.instagram
DES-CFB8
boringssl_context_alert_callback_handler
Ba
RSA-SHA224
ssl->s3->write_level == level
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/s3_pkt.cc
com.squareup.cash
fe_mul_impl
TLS client send_client_certificate_verify
psk_len <= PSK_MAX_PSK_LEN
redacted
algorithm %d
group->field.N.width == group->order.N.width
CBS_len(&copy) == 0
com.soda.music
crlBag
Acceptable OCSP Responses
janetMailbox
no certificate
RSA_decrypt
words > 0
invalidityDate
ISO
id-smime-cd
id-it-encKeyPairTypes
id-cmc-queryPending
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/d1_both.cc
com.google.Sheets
DTLSv1_get_timeout
peer_public_key_type
OBJ_LIB
id-pda-gender
do_select_parameters
TLS client finish_flight
boringssl_ciphers_copy_supported_list_for_groups
certificate revoked
com.cmbchina.MPBBank
boringssl_helper_create_sec_trust_with_certificates
TLSConnectionEvent
RSA-MD2
sect113r2
ssl_run_handshake
MLKEM768_generate_key
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc
boringssl_private_key_sign
KYBER_encap
-BN_MUL_RECURSIVE_SIZE_NORMAL/2 <= dna && dna <= 0
id-HMACGostR3411-94
id-GostR3410-2001-TestParamSet
com.spotify.client
public key routines
cast5-cbc
id-mod-dvcs
d1_pkt.cc
alg=%d
com.southwest.iphoneprod
alpn_used
User defined functions
des-ede3-ofb
c2pnb272w1
KxANY
MLKEM768_decap
id-smime-aa-macValue
TLS_PSK_WITH_AES_256_CBC_SHA
system library
CRYPTO
bf-ecb
id-mod-ocsp
OCSP Archive Cutoff
trustRoot
gost94
HEAD 
boringssl_session_state_copy_serialized_session_state
com.remind101.Remind101
md_size <= EVP_MAX_MD_SIZE
setCext-TokenIdentifier
seed-ecb
!hs->new_session
nw_protocol_boringssl_error
RSA-SHA1
id-mod-crmf
documentVersion
setct-CapTokenSeq
boringssl_session_set_state
decryption failed
!hs->ssl->server
com.bankabc.iphonerelease
0 < w && w <= 7
RC4
pbeWithSHA1And40BitRC4
Private
EXPORTER_EAP_TLS_Key_Material
net.kortina.labs.Venmo
international-organizations
Open
ats_non_pfs_ciphersuite_allowed
printf.c
aes-256-ofb
setct-CapTokenTBE
dmdName
curve25519.c
nonce_len >= 8
com.etsy.etsyforios
r != a
id-smime-cd-ldap
decode error
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/dtls_method.cc
id-pkix-mod
id-it-preferredSymmAlg
setct-AuthRevResTBS
i == count
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc
camellia-256-ecb
in->digest->ctx_size != 0
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc
com.einnovation.temu
com.amazon.Amazon
X509v3 Freshest CRL
userPassword
num_words <= INT_MAX
boringssl_crypto_hash_nid_to_cc_digest
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc
EVP_CIPHER_CTX_mode(&tls_ctx->cipher_ctx) != EVP_CIPH_CBC_MODE
tls13_client.cc
!inc
dhKeyAgreement
com.facebook.Facebook
com.supercell.scroll
sbgp-autonomousSysNum
cmac
aes-192-gcm
requested=%u
level == SSL3_AL_FATAL
tls_dispatch_alert
dNSDomain
Microsoft Local Key set
!chunk.empty()
com.weather.TWC
com.boc.BOCMBCI
O
setAttr-GenCryptgrm
handshake failure
ctx->digest->md_size <= EVP_MAX_MD_SIZE
com.midasplayer.apps.candycrushsaga
client_mode
extendedStatus
pilotGroups
c2pnb176v1
boringssl_context_keylog_handler
ssl_privkey.cc
aaControls
GOST 34.10-94 Cryptocom
brainpoolP512r1
ssl->s3->version == 0
TLS client send_client_certificate
tls1_P_hash
bn_mod_u16_consttime
com.blitzstudios.sleeperbot
com.nhncorp.m2app
aes-256-cfb
set-addPolicy
brainpoolP384r1
TLS client read_server_key_exchange
AES256-GCM-SHA384
nw_protocol_boringssl_initiate_pqtls_fallback_block_invoke
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_privkey.cc
com.ubercab.UberEats
DSA-old
id-it-signKeyPairTypes
ECDHE-PSK-AES128-CBC-SHA
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_buffer.cc
org.iggymedia.periodtracker
id-GostR3410-2001-CryptoPro-A-ParamSet
kx-any
TLS 1.3 server read_client_encrypted_extensions
id-pkix1-explicit-88
CLIENT_RANDOM
EVP_EncryptUpdate
in->pctx == NULL || in->pctx_ops != NULL
com.meitu.mtxx
ech_used
OCSP_LIB
SSL_CIPHER_get_protocol_id
B16@?0@\"NSObject<OS_nw_frame>\"8
ssl->s3->initial_handshake_complete == !ssl->s3->previous_client_finished.empty()
snmpv2
ucl
wap
TLS 1.3 server select_session
DTLSv1
tv.twitch
unstructuredName
SHA512-256
ssl_aead_ctx.cc
Server
nw_protocol_boringssl_output_available
md4
setct-AuthResTBS
st->depth > 0
boringssl_helper_zlib_compress_data
rc4
Netscape Communications Corp.
id-mod-cmc
id-cmc-responseInfo
Hold Instruction Call Issuer
data
ssl->s3->pending_flight_offset == 0
supportedAlgorithms
AES-192-CBC-HMAC-SHA1
boringssl_context_evaluate_trust_async_external
negotiate_version
b <= sizeof(ctx->final)
dtls1_write_record
ECDSA-X962-SHA224
sect571k1
TLS_ECDHE_ECDSA_WITH_DES_192_CBC3_SHA
boringssl_session_client_psk_callback_handler
bytes_written == 2
encrypted_client_hello.cc
DSA_LIB
EVP_DecryptUpdate
EdDSA-Curve25519-SHA512
borrow == 0
id-it-caProtEncCert
seed-ofb
TLS server done
constant_time_declassify_int(bn_in_range_words(r->d, min_inclusive, max_exclusive->d, words))
certificatePolicies
wap-wsg-idm-ecid-wtls1
boringssl_context_should_log_ATS_trust_eval_warning
ssl_get_prev_session
BN_CTX_free
PASSED_NULL_PARAMETER
Netscape Base Url
pbeWithSHA1And2-KeyTripleDES-CBC
id-ad
lastModifiedBy
boringssl_context_set_ats_minimum_signature_algorithm
aECDSA
len == 0 || (in != NULL && out != NULL)
mask != 0
lib(%u)
timeStamping
Microsoft Individual Code Signing
cleartext track 2
record overflow
hs->new_cipher == session->cipher
des-ede-cfb
PBE-SHA1-RC4-128
RSA-MD4
ipsec4
CAMELLIA-256-CFB
id-GostR3410-94-CryptoPro-XchA-ParamSet
id-smime-aa-contentReference
setct-CertReqData
ssl_session_protocol_version(hs->early_session.get()) >= TLS1_3_VERSION
window_val == 0
ats_minimum_rsa_key_size
aes-128-cfb
c2tnb191v3
ext_ri_add_clienthello
ECDSA_verify
!needs_psk_binder
BF-ECB
secp112r1
ssl->s3->established_session == nullptr
MLKEM768_parse_public_key
TRUST_TOKEN
id-mod-qualified-cert-88
org
setext-genCrypt
id-Gost28147-89-CryptoPro-D-ParamSet
(NONE)
ext_ticket_add_serverhello
DES-EDE3-OFB
id-GostR3410-94-a
boringssl_session_write
cb_ret == 1
Decap
id-cmc-popLinkWitness
boringssl_context_evaluate_trust_async_external_block_invoke
!buffers_alias(dst, n, src, n)
do_finish_client_handshake
com.phoenix.video
cipher_name
group_name
com.soundcloud.TouchApp
unknown_negotiated_protocol
qualityLabelledData
Microsoft Smartcardlogin
c2onb191v5
brainpoolP384t1
boringssl_context_set_min_version
com.offerup.iphone.consumer
EVP_LIB
X509v3 Certificate Policies
id-on
setct-PANToken
ECDH-RSA-AES256-SHA
ssl_handshake_new
bf-ofb
EC_KEY_set_group
com.ticketmaster.ios.TicketmasterApp
domainComponent
room
c2tnb431r1
A `
insufficient security
p <= 16
err.c
ECDH_LIB
id-characteristic-two-basis
constant_time_declassify_int(out[_assert_fe_i] <= (0x8ccccccccccccULL))
bn.c.inc
client EAP encryption
boringssl_session_copy_authenticator_trust
TLS 1.3 server send_hello_retry_request
block_size <= sizeof(key_block)
AES-192-CBC
setct-CapRevReqTBS
ECDHE-RSA-AES128-SHA
SSLv3
doordash.DoorDashConsumer
private key operation incomplete
nsBaseUrl
SN
setct-BCIDistributionTBS
TLS client read_certificate_status
ECDH-RSA-DES-CBC3-SHA
ext_quic_transport_params_add_clienthello_impl
constant_time_declassify_int(c == 0)
com.dragon.read
X509v3 Basic Constraints
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/evp.c
pkcs7-signedAndEnvelopedData
rc2-64-cbc
id-regCtrl-protocolEncrKey
out
id-smime-aa-ets-CertificateRefs
boringssl_context_set_legacy_ats_applicable
ssl_protocol_version(ssl) < TLS1_3_VERSION
HPKE
EC_GROUP_get0_order
boringssl_psk_cache_lookup_psk_block_invoke_2
generate cryptogram
secp224r1
hmacWithSHA384
SSL_CIPHER_get_digest_nid
TLS 1.3 server read_second_client_flight
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc
used_legacy_codepoint == hs->config->quic_use_legacy_codepoint
cbb->child == NULL
AES-128-CFB
AES-128-CTR
dhSinglePass-stdDH-sha384kdf-scheme
access denied
t1_enc.cc
bn_neg_inv_mod_r_u64
com.beeasy.shopee.vn
rc2-cbc
basicOCSPResponse
wvalue < (1 << window)
setct-CRLNotificationResTBS
!ssl->server
com.google.Chromecast
PBE-SHA1-3DES
setext-pinSecure
TLS client read_server_hello_done
hs->min_version > TLS1_2_VERSION
CBB_len
set-policy-root
AES-128-CFB8
STRENGTH
com.bot.doubao
constant_time_declassify_int(carry + 1 <= 1)
basicConstraints
mdc2
id-Gost28147-89-CryptoPro-KeyMeshing
id-GostR3411-94-with-GostR3410-2001-cc
ST
SEED-OFB
aead_chacha20_poly1305_seal_scatter
mac_key_len <= EVP_MAX_MD_SIZE
GET 
com.apple.WebKit
id-aes256-CCM
TLS_ECDHE_RSA_WITH_DES_192_CBC3_SHA
!hs->pake_participant
no_bundle_id
tls_cbc.c
ssl_encrypt_client_hello
id-smime-aa-ets-signerLocation
boringssl_context_set_key_exchange_groups_from_list
boringssl_context_set_is_local_networking
TLS_AES_128_GCM_SHA256
com.google.calendar
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m
dtls
id-smime-aa-smimeEncryptCerts
boringssl_context_set_max_version
EXPORTER-server authenticator handshake context
setCext-setExt
dhSinglePass-cofactorDH-sha256kdf-scheme
TLS_RSA_WITH_AES_256_GCM_SHA384
!BN_is_zero(&mont->N)
com.amazon.echo
Diffie-Hellman routines
SXNetID
camellia-192-ecb
id-GostR3410-94-CryptoPro-XchB-ParamSet
id-GostR3410-94-aBis
boringssl_session_server_psk_callback_handler
sha384
boringssl
TLS 1.3 client send_client_certificate_verify
com.indeed.JobSearch
d0 & (((BN_ULONG)1) << (BN_BITS2 - 1))
session_resumed
id-cmc-popLinkRandom
id-aes128-wrap-pad
v28@?0^{__SecTrust=}8B16^{__CFError=}20
boringssl_context_set_encryption_secrets_block_invoke
TLS client early_reverify_server_certificate
SHA256
reason(%u)
S/MIME
id-mod-kea-profile-93
id-ppl-independent
sect193r2
gost2001cc
d1_both.cc
ssl->d1->mtu >= dtls1_min_mtu()
TLS 1.3 client send_client_encrypted_extensions
com.nestlabs.jasper.release
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_key_share.cc
SetupContext
ECDSA routines
Microsoft Trust List Signing
aead_tls_tag_len
id-it-origPKIMessage
account
setct-PInitResData
got type %d, wanted type %d
sha1WithRSAEncryption
com.siwuai.duapp
destroyed
caIssuers
id-smime-cti-ets-proofOfSender
camellia-256-cfb
PSK-AES256-CBC-SHA384
ber.c
des-ede3-cfb8
3DES
SSL negotiation finished successfully
unsupported extension
ssl_protocol_version(hs->ssl) < TLS1_3_VERSION
com.hulu.plus
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_lib.cc
print_errors_to_file
associatedName
md_gost94
com.overdrive.dewey
ticket_received
des-ede
mime-mhs
wap-wsg-idm-ecid-wtls6
variable_nonce_included_in_record_
TLS 1.3 server process_end_of_early_data
TLS 1.3 client complete_second_flight
waiting to connect
connected
id-smime-aa-encrypKeyPref
fe_sq_tl
nope
bn_reduce_once
ticket_enabled
X509v3 Policy Mappings
GOST R 34.11-94
d1_srtp.cc
now.tv_sec >= session->time
ECDHE-ECDSA-DES-CBC3-SHA
SSL_get_srtp_profiles
boringssl_context_handle_handshake_timer
info_hash
com.microsoft.skype.teams
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/p_ed25519.c
safeContentsBag
x509Certificate
setct-PANData
c2pnb163v2
rsa
msSGC
wap-wsg-idm-ecid-wtls10
GOST R 34.10-94 DH
TLSv1/SSLv3
PSK-AES256-GCM-SHA384
CLIENT_EARLY_TRAFFIC_SECRET
RSA-PKCS1v15-SHA512
sect131r1
id-GostR3411-94-with-GostR3410-94-cc
boringssl_bio_create
md_len % 8 == 0
TLS 1.3 client send_client_certificate
id-pkix1-implicit-88
noCheck
ex_data.c
B16@?0^v8
boringssl_crypto_digests.m
KYBER_generate_key
com.crossforward.WidgetSmith
rc5-ecb
KISA
id-PasswordBasedMAC
boringssl_context_evaluate_trust_async_internal_log_only
nw_protocol_boringssl_read_frames
icloud.com
ENGINE
NIST P-384
RC2-40-CBC
GN
CAMELLIA-128-CFB1
constant_time_declassify_int(h->v[_assert_fe_i] <= (0x1a666666666664ULL))
mac_len == HMAC_size(&tls_ctx->hmac_ctx)
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/bio/bio_mem.c
OCSP
des-ede3
algorithm
AES-192-ECB
camellia-192-cfb8
boringssl_context_zlib_compress_data_block_invoke
v12@?0I8
!skip
com.google.ios.youtubekids
apple.com
id-DHBasedMac
id-GostR3411-94-CryptoProParamSet
dhSinglePass-stdDH-sha1kdf-scheme
dh-std-kdf
frag->seq == msg_hdr->seq
com.deepseek.chat
RSA-PKCS1v15-MD5
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/d1_lib.cc
MALLOC_FAILURE
pilotPerson
hs->ssl->ctx->reverify_on_resume
kECDHE
s3_both.cc
directory services - algorithms
nameConstraints
TLS server send_server_key_exchange
num_funcs <= (size_t)(INT_MAX - ex_data_class->num_reserved)
ext_ri_parse_clienthello
com.google.Docs
com.laiwang.DingTalk
handshake_timer_fires
NIST P-521
setct-CredReqTBSX
CAMELLIA-192-ECB
v8@?0
nw_protocol_boringssl_disconnect
min_version
authorityInfoAccess
id-smime-aa-ets-RevocationRefs
aes-128-cfb8
GOST 28147-89 MAC
EDH-RSA-DES-CBC3-SHA
boringssl_session_handshake_incomplete
SharedKey
crlNumber
title
nw_protocol_boringssl_input_available
BUF_LIB
object identifier routines
IDEA-ECB
AES-192-CFB
setct-BatchAdminReqData
setCext-setQualf
id-ct-asciiTextWithCRLF
sha256
orig_len >= in_len
dcobject
des-cfb1
wap-wsg
crossCertificatePair
ssl_cipher.cc
TLS_RSA_WITH_NULL_SHA
frame full
')
n % 2 == 1
extendedKeyUsage
boringssl_context_evaluate_trust_async_internal_log_only_block_invoke_2
PBES2
DOD
anyPolicy
 
ticket.size() >= SSL_TICKET_KEY_NAME_LEN + EVP_MAX_IV_LENGTH
tls_add_message
com.att.osd.myWireless
lo == hi
id-it-revPassphrase
CAMELLIA-256-CFB1
brainpoolP192r1
ECDH_compute_key
ats_minimum_signature_algorithm
ERR_save_state
id-on-personalData
certificateIssuer
prf-gostr3411-94
boringssl_context_set_ciphersuites_from_string
bad certificate status response
tls13_process_finished
com.dianping.dpscope
window_val <= next_bit
sect233k1
!top
id-smime-spq-ets-sqt-uri
id-qt
ipsecUser
id-alg-des40
X25519Kyber768Draft00
ECDH-ECDSA-AES128-SHA
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/tls13_enc.cc
TLS 1.3 server read_client_finished
com.dunkinbrands.otgo
RU.WILDBERRIES.MOBILEAPP
gost-mac
tls13_export_keying_material
ssl_private_key_sign
!ssl->s3->aead_write_ctx->is_null_cipher()
CRLReason
bl <= (int)sizeof(ctx->buf)
n != 0 && (n & (n - 1)) == 0
disconnecting
ASN1
RC2-64-CBC
Diffie-Hellman based MAC
AES-256-XTS
session unavailable
documentPublisher
com.target.Target
com.viber
HMAC_LIB
id-smime-aa-timeStampToken
id-smime-aa-ets-signerAttr
ecdsa-with-SHA224
aes-128-ctr
TLS 1.3 server done
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_cert.cc
SEED-CFB
brainpoolP160t1
CRYPTO_chacha_20
TLS_PSK_WITH_AES_128_GCM_SHA256
constant_time_declassify_int(carry <= 1)
co.hinge.mobile.ios
DES-EDE-CBC
RC5-ECB
Policy Qualifier CPS
GOST R 3410-2001 Parameter Set Cryptocom
id-camellia192-wrap
CHACHA20
hex_char_consttime
secret_for_quic.empty()
id-qcs
nw_protocol_boringssl_write_bytes
add_outgoing
HMAC_Init_ex
cl >= 0
pinterest
ECDH routines
des-cbc
AES-128-OFB
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/hpke/hpke.c
ret
works.jubilee.timetree
rc5-cfb
GOST 34.10-2001 Cryptocom
Permanent Identifier
AES-128-XTS
brainpoolP256t1
RSA
com.chase
com.ucweb.iphone.lowversion
EC_LIB
CAMELLIA-128-OFB
subjectDirectoryAttributes
tls13_add_certificate_in_buffer
cert_compression_used
pkcs7
id-pkix1-implicit-93
aes-192-cfb
setct-AuthRevResTBE
wap-wsg-idm-ecid-wtls4
ChaCha20-Poly1305
nw_protocol_boringssl_disconnected
bytes_written <= to_write
in_len >= md_size
X509v3 Issuing Distribution Point
TLS_ECDH_ECDSA_WITH_DES_192_CBC3_SHA
rsa_default_sign_raw
rc5-ofb
brainpoolP224r1
certificate unobtainable
ext_sct_parse_serverhello
ext_channel_id_parse_serverhello
incoming_byte_count
PBE-MD5-DES
caseIgnoreIA5StringSyntax
setct-CredRevReqTBSX
TLS client finish_client_handshake
dtls1_hm_fragment_mark
len == hs->secret.size()
jp.pay2.app.ios
ssl_lib.cc
aes-256-ecb
sha512
unknown CA
ssl->s3->version != 0
!ssl->s3->pending_hs_data
nw_protocol_boringssl_write_frames_block_invoke
group_
id-cmc-addExtensions
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/mem.c
boringssl_crypto_aes.m
sbgp-ipAddrBlock
domainRelatedObject
seed-cbc
ECDHE-RSA-AES128-SHA256
targetInformation
nw_protocol_boringssl_get_output_frames
sha512_final_impl
TLS 1.3 server read_channel_id
TLS 1.3 client read_server_finished
id-pkip
pilotAttributeType
c2tnb191v1
boringssl_context_zlib_uncompress_data_block_invoke
n_bits != 0
RSA-PKCS1v15-SHA384
id-it-currentCRL
set-certExt
secp521r1
hs->wait != ssl_hs_read_change_cipher_spec
nw_protocol_boringssl_get_input_frames_block_invoke
ssl_cert.cc
street
sect163r2
ext_key_share_add_clienthello
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c
ALL
ssl->config
setct-AuthReqTBS
AES-256-CFB1
camellia-128-cfb8
id-GostR3410-2001-ParamSet-cc
name
Subject Information Access
TLS 1.3 server send_new_session_ticket
IDEA-CFB
PBE-MD5-RC2-64
id-smime-cti-ets-proofOfOrigin
ac-targeting
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/p_ed25519_asn1.c
@`
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc
BIO_LIB
id-pda-placeOfBirth
setct-AuthResTBEX
RC4-HMAC-MD5
RSA_padding_check_PKCS1_OAEP_mgf1
close_early_data
EXPORTER-client authenticator finished key
handshake_rtt
dsaEncryption
qcStatements
id-ppl
id-Gost28147-89-CryptoPro-RIC-1-ParamSet
aes-256-xts
boringssl_session_handshake_start
RSA-MD5
digit & 1
SSL_get_psk_identity_hint
write_stalls
legacy_ats_nonpfs
TRUST_TOKEN_LIB
RC4-40
md5WithRSAEncryption
internal.h
challenge_block_used
connection_id
nsComment
X9.57
proxyCertInfo
constant_time_declassify_int(in2[_assert_fe_i] <= (0x1a666666666664ULL))
tls_seal_scatter_record
com.xunmeng.pinduoduo
id-smime-ct-DVCSRequestData
id-cmc-recipientNonce
AD_DVCS
setct-OIData
dsa_with_SHA256
write
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/d1_pkt.cc
n < block_size
com.facebook.Messenger
com.ss.iphone.ugc.Aweme
com.ulta.UltaMcommerceApp
alert_code
out_len == requested_len
aes-128-gcm
NONE
messageDigest
nsRevocationUrl
clearance
document
brainpoolP192t1
boringssl_context_new_session_handler_block_invoke
TLS server read_client_key_exchange
`
set-brand-IATA-ATA
hs != nullptr
ECDH-RSA-AES128-SHA
fixed_iv.size() >= aead_ctx->variable_nonce_len_
ssl_parse_extensions
connection was shut down
GOST 28147-89
id-Gost28147-89-CryptoPro-C-ParamSet
ECDHE-RSA-CHACHA20-POLY1305
HIGH
iv
com.jiangjia.gif
dsa
setct-AuthTokenTBS
GOST R 34.10-2001 DH
com.tencent.ww
X509v3 AC Targeting
friendlyCountryName
mime-mhs-headings
constant_time_declassify_int(f->v[_assert_fe_i] <= (0x1a666666666664ULL))
B`
secret
X509v3 Key Usage
id-cmc-encryptedPOP
setct-AcqCardCodeMsgTBE
hmac-md5
UI routines
msg[msg_len] == '\\0'
id-smime-alg-ESDHwithRC2
prime192v2
set-brand-Visa
SEED-ECB
id-aes256-GCM
lgBigR >= n_bits
ipsecTunnel
TLSBiomeConnectionEvent
joint-iso-itu-t
c2tnb239v2
TLS client read_server_finished
boringssl_helper_dump_buffer
EXPORTER-client authenticator handshake context
legacy_ats_applicable
UI_LIB
searchGuide
fatal
com.united.UnitedCustomerFacingIPhone
id-smime-mod-ets-eSignature-88
DVCS
aes-128-ecb
ssl_send_tls12_certificate
RSA_sign_pss_mgf1
com.wbd.stream
com.google.Tachyon
pkcs
RSA Data Security, Inc. PKCS
BF-OFB
CAST5-CFB
pseudonym
v20@?0@\"boringssl_concrete_boringssl_ctx\"8B16
!buffers_alias(in, in_len, out_prefix, ssl_record_prefix_len(ssl))
compress != nullptr || decompress != nullptr
invalid library (0)
RC2-OFB
id-it-unsupportedOIDs
setct-PCertResTBS
TLS server read_client_certificate_verify
TLS 1.3 client read_encrypted_extensions
PKCS7
PEM_LIB
id-it-subscriptionRequest
pilotDSA
otherMailbox
setct-AuthRevResTBEB
aes-192-ccm
TLS 1.3 server read_second_client_hello
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/cipher_extra/e_tls.c
com.tencent.xin
DSA routines
nsSslServerName
pkcs1
Experimental
TLS client read_certificate_request
missing extension
hs->scts_requested
com.baidujp.Simeji.SimejiKB
localKeyID
policyConstraints
camellia-256-cfb1
num <= BN_MAX_WORDS
msg_len > 0
boringssl_helper_copy_certificates_from_session
PBE-SHA1-2DES
secp384r1
GOST R 34.10-2001
uniqueMember
do_read_session_ticket
B40@?0@\"NSObject<OS_dispatch_data>\"8Q16r^v24Q32
MLKEM768_encap
negotiated_protocol
cbs_get_any_asn1_element
id-smime-aa-ets-sigPolicyId
id-qcs-pkixQCSyntax-v1
boringssl_context_set_alpn_protocol_list
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc
com.expedia.booking
Netscape Server Gated Crypto
id-smime-aa-dvcs-dvc
personalTitle
setct-CapRevReqTBEX
ED25519
com.yahoo.ffootball2009
X509v3 CRL Reason Code
id-smime-aa-ets-contentTimestamp
id-alg-PWRI-KEK
SSL_get_session
do_send_half_rtt_ticket
com.pnc.pncmobile
rc4-40
enhancedSearchGuide
ConfirmationKeys
felem.c.inc
id-pe
lastModifiedTime
psk_id_hash
C
Mail
c2tnb239v1
TLS server send_server_hello_done
nw_protocol_boringssl_connected
cn.10086.app
0 <= window_val && window_val <= next_bit
alert_type
dsaWithSHA1
*out_len == EVP_MD_size(digest)
ECDSA-X962-SHA256
elliptic curve routines
HKDF functions
kisa
align_pointer
KYBER_parse_public_key
com.google.Maps
mid + 1 < hi
tls_compliance_policy
des-ecb
id-smime-aa-msgSigDigest
TLS server send_server_certificate
.local
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/extensions.cc
overflow
id-smime-mod
id-regCtrl
set-attr
sect131r2
dhpublicnumber
cbb->u.base.can_resize
add_record_to_flight
lh->num_buckets >= kMinNumBuckets
idea-ecb
keyUsage
AD Time Stamping
setct-PIDualSignedTBE
setAttr-IssCap-T2
Dup
SYS
idea-cbc
id-mod-kea-profile-88
id-regCtrl-authenticator
IANA
setct-CertReqTBS
camellia-128-ofb
unexpected_message
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/p_rsa_asn1.c
com.apple.
com.chipotle.Chipotle
RSA-PKCS1v15-SHA224
setct-PIData
AuthECDSA
alg_k & SSL_kPSK
nw_protocol_boringssl_replace_input_handler
RSA_LIB
SSL routines
!(string_tag & CBS_ASN1_CONSTRUCTED)
pbeWithMD2AndDES-CBC
pbeWithSHA1AndRC2-CBC
PBE-SHA1-RC2-128
id-smime-aa-ets-certValues
digest_init
B24@?0Q8@\"NSObject<OS_sec_object>\"16
bad certificate
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc
configured_ciphersuites
iA5StringSyntax
payment gateway capabilities
id-Gost28147-89-CryptoPro-B-ParamSet
dtls1_next_message
TLS 1.3 client send_second_client_hello
TLS 1.3 client done
hs->config->channel_id_private
com.ring
X509v3 Authority Key Identifier
setext-cv
do_send_server_certificate
com.wf.mobilebanking
ssl_ctx_get_current_time
server_name
friendlyCountry
TLS client reverify_server_certificate
dtls1_set_write_state
id-smime-aa-contentHint
CrlID
dtls1_update_mtu
id-cct-crs
issuer capabilities
ICC or token signature
PSPECIFIED
boringssl_context_log_message
ec_point_to_bytes
HMAC
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_asn1.cc
tls1_check_duplicate_extensions
*out == NULL
BUF
issuingDistributionPoint
TLS_PSK_WITH_AES_256_CBC_SHA384
boringssl_session_set_peer_verification_state_from_session
cipher.c.inc
al >= j && bl >= j
com.creditkarma.mobile
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/buf/buf.c
wap-wsg-idm-ecid-wtls12
hs->credential->type == SSLCredentialType::kX509
nw_protocol_boringssl_allocate_batching_frame
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc
ssl_tls13_cipher_meets_policy
len <= EC_MAX_BYTES
boringssl_session_set_ech_config
CRYPTO_LIB
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc
serviceLocator
path
sect193r1
sect233r1
aes-128-cbc-hmac-sha1
ssl_record_prefix_len
ext_quic_transport_params_add_serverhello_impl
boringssl_session_state_create
HKDF_LIB
certBag
Security
bn_words_to_big_endian
AES
userClass
setct-PCertReqData
X509v3 Inhibit Any Policy
destinationIndicator
!ssl->s3->used_hello_retry_request
pqtls_used
lh_maybe_resize
set-brand-Novus
fixed_iv.size() <= aead_ctx->variable_nonce_len_
boringssl_session_set_peer_hostname
bssl_test
id-Gost28147-89-CryptoPro-Oscar-1-0-ParamSet
seeAlso
TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA
RSA-SHA512
NA
id-smime-aa-signatureType
subtreeMinimumQuality
setCext-IssuerCapabilities
sn
com.life360.safetymap
grease_enabled
RSA-RIPEMD160
ipsecEndSystem
auth-rsa
kRSA
nw_protocol_boringssl_remove_input_handler
com.google.paisa
waiting for data to read
EC
id-GostR3410-2001-CryptoPro-B-ParamSet
fe_frombytes_strict
TLS_RSA_WITH_AES_256_CBC_SHA
com.amazon.aiv.AIVApp
com.audible.iphone
com.adp.adpmobile
com.vk.vkclient
handshake_cancelled
id-smime-ct-authData
id-GostR3410-94-CryptoPro-B-ParamSet
roleOccupant
false_start_used
auth-ecdsa
TLS_AES_256_GCM_SHA384
boringssl_session_handshake_negotiate
com.bankofamerica.BofA
com.costco.costco
id-aes128-GCM
ext_npn_parse_serverhello
parse_integer
com.capitalone.enterprisemobilebanking
ec_GFp_mont_mul_public_batch
boringssl_metrics_create_connection_event
directory services (X.500)
id-hex-multipart-message
gost2001
set
Client
nw_protocol_boringssl_get_input_frames
inappropriate fallback
do_select_session
boringssl_session_state_create_from_dispatch_data
com.groupme.iphone-app
USER_LIB
boringssl_session_handshake_continue_inner
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/ssl/ssl_versions.cc
lo <= mid && mid < hi
DH_LIB
CBS_get_asn1_implicit_string
without
RIPEMD160
boringssl_context_log_potential_ats_violation_negotiated_ciphersuite
ssl_protocol_version(ssl) == TLS1_3_VERSION
ssl
id-smime-aa-signingCertificate
boringssl_context_update_potential_ATS_violations
TLS 1.3 server read_client_certificate_verify
j <= al || j <= bl
ECDH
setct-CredRevReqTBS
setct-CredReqTBE
preferredDeliveryMethod
!ignore_unknown
md5-sha1
bignum routines
Netscape Cert Type
ad_timestamping
Extended OCSP Status
ECDH-ECDSA-DES-CBC3-SHA
nw_protocol_boringssl_handshake_negotiate
CRYPTO_BUFFER_free
ctx->tag_len
RSA_padding_add_PKCS1_OAEP_mgf1
field_len == BN_num_bytes(&group->field.N)
commonName
id-smime-aa-ets-otherSigCert
FIPS
nw_protocol_boringssl_initiate_pqtls_fallback
boringssl_ecdsa_get_cc_curve_parameters
setct-CapReqTBEX
TLS server unknown
invalid
OCSP routines
CN
rc2-ofb
id-alg-dh-sig-hmac-sha1
dod
setct-MeAqCInitResTBS
asn1_compat.c
tls_write_app_data
with
des-ede-cbc
Proxy Certificate Information
MGF1
CRYPTO_free_ex_data
com.meituan.imeituan
id-smime-aa
id-cmc-getCert
id-GostR3410-2001-CryptoPro-XchB-ParamSet
KxRSA
handshake.cc
yes
frag->msg_len == msg_len
!hs->key_share_bytes.empty()
com.hammerandchisel.discord
psk_configured
streetAddress
TLS_EDH_RSA_WITH_3DES_EDE_CBC_SHA
boringssl_context_start_handshake_timer
Cipher functions
id-aca-accessIdentity
id-cct-PKIData
prime239v1
prime239v3
pilotObjectClass
setCext-merchData
b <= sizeof(ctx->buf)
com.reddit.Reddit
wNAF_len <= OPENSSL_ARRAY_SIZE(g_wNAF)
EVP
sect239k1
CAMELLIA-192-CFB1
hmacWithSHA512
SealScatter
crlDistributionPoints
1`
boringssl_context_info_handler
kPSK
com.baidu.BaiduMobile
id-it-caKeyUpdateInfo
ad dvcs
setct-CapRevReqTBE
EVP_MD_CTX_cleanup
UID
X509v3 Name Constraints
cipher->algorithm_mac == SSL_SHA1
AES128-SHA
boringssl_ciphers_create_configuration_string
-bit < digit && digit < bit
CBS_get_optional_asn1_octet_string
pbeWithMD2AndRC2-CBC
2`
immediate mode
ab
com.usablenet.walgreens
X509v3 Private Key Usage Period
id-smime-ct
id-smime-aa-receiptRequest
id-aca
id-pda-dateOfBirth
ECDSA-X962-SHA512
id-regCtrl-pkiArchiveOptions
roomNumber
bn_set_static_words
MD5
md32_common.h
rc2-cfb
boringssl_context_update_encryption_level_block_invoke
rsa_asn1.c
com.autonavi.amap
tv.lifechurch.bible
CONF_LIB
Netscape Certificate Extension
id-cmc-dataReturn
id-aca-group
protocol version
SERVER_TRAFFIC_SECRET_0
len + block_size - early_mac_len == in_len
boringssl_helper_copy_certificates_from_CRYPTO_BUFFERs
Netscape Comment
AES-128-CFB1
ecdsa-with-Recommended
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/evp/evp_ctx.c
do_read_hello_retry_request
ext_ri_parse_serverhello
dtls_method.cc
com.apple.network.boringssl.metrics_queue
aes-128-ofb
setct-PI
pSpecified
lhash.c
RC5-OFB
id-pda-countryOfResidence
id-ppl-anyLanguage
com.apple.network.boringssl.user_interactive_qos_trust_queue
bytes_written == 0 || bytes_written_compressed == 0
com.tencent.smoba
setct-CRLNotificationTBS
id-GostR3410-2001-CryptoPro-XchA-ParamSet
ECDHE-ECDSA-AES128-SHA
ECDHE-RSA-DES-CBC3-SHA
SSL
com.instructure.icanvas
com.immediasemi.ios.blink
dvcs
directory
aes-192-cbc
id-aes256-wrap
ECDHE-RSA-AES256-SHA
/Library/Caches/com.apple.xbs/C094FC1E-5E2B-4B34-9BDD-299E93B35D5C/TemporaryDirectory.avjUm9/Sources/boringssl/crypto/bn_extra/bn_asn1.c
socket
!hs->config->alps_configs.empty()
ctrip.com
iso
wap-wsg-idm-ecid-wtls5
id-GostR3411-94-with-GostR3410-2001
RSAES-OAEP
com.netease.cloudmusic
com.ccb.ccbDemo
rfc822Mailbox
boringssl_context_handle_fatal_alert
TLS_CHACHA20_POLY1305_SHA256
ECDHE-ECDSA-AES256-GCM-SHA384
is_string_type(inner_tag)
boringssl_context_copy_peer_sct_list_from_extension
cipher->algorithm_enc & (SSL_AES128GCM | SSL_AES256GCM)
TLSv1.1
POST 
com.particlenews.newsbreak
md2WithRSAEncryption
pilot
id-aes192-wrap
ctx->used == 0 || ctx->error
com.myliftmaster.myq
pqtls_enabled
Policy Qualifier User Notice
Selected Attribute Types
characteristic-two-field
set-brand
wap-wsg-idm-ecid-wtls11
nil
```
