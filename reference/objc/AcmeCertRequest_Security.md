# `AcmeCertRequest`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 36 instance variables, 36 properties, 93 instance methods, 0 class methods

## Instance variables

```
B _logAcmeCSR;
B _permitLocalIssuer;
B _requireAttestation;
q _state;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSArray" _subject;
@"NSDictionary" _parameters;
@"NSDictionary" _keyParams;
@"NSArray" _attestationOids;
@"NSArray" _attestationChain;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _attestationCRKey;
@"NSArray" _attestationCRChain;
@"NSData" _attestation;
@"NSData" _csr;
@"NSString" _nonce;
@"NSString" _location;
@"NSString" _account;
@"NSString" _token;
@"NSString" _timestamp;
@"NSArray" _authorizations;
@"NSString" _authorizationURL;
@"NSString" _challengeURL;
@"NSString" _finalizeOrderURL;
@"NSString" _orderURL;
@"NSString" _certificateURL;
@"NSString" _nextMessageURL;
@"NSString" _acmeNewAccountURL;
@"NSString" _acmeNewNonceURL;
@"NSString" _acmeNewOrderURL;
@"NSObject<OS_dispatch_queue>" _xpc_queue;
@"NSObject<OS_xpc_object>" _connection;
@"SecJWSEncoder" _encoder;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _publicKey;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _privateKey;
^{__SecCertificate=} _certificate;
^{__SecIdentity=} _identity;
```

## Properties

```
@property (Tq,V_state) state;
@property (TB,V_logAcmeCSR) logAcmeCSR;
@property (TB,V_permitLocalIssuer) permitLocalIssuer;
@property (TB,V_requireAttestation) requireAttestation;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@"NSArray",&,V_subject) subject;
@property (T@"NSDictionary",&,V_parameters) parameters;
@property (T@"NSDictionary",&,V_keyParams) keyParams;
@property (T@"NSArray",&,V_attestationOids) attestationOids;
@property (T@"NSArray",&,V_attestationChain) attestationChain;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_attestationCRKey) attestationCRKey;
@property (T@"NSArray",&,V_attestationCRChain) attestationCRChain;
@property (T@"NSData",&,V_attestation) attestation;
@property (T@"NSData",&,V_csr) csr;
@property (T@"NSString",&,V_nonce) nonce;
@property (T@"NSString",&,V_location) location;
@property (T@"NSString",&,V_account) account;
@property (T@"NSString",&,V_token) token;
@property (T@"NSString",&,V_timestamp) timestamp;
@property (T@"NSArray",&,V_authorizations) authorizations;
@property (T@"NSString",&,V_authorizationURL) authorizationURL;
@property (T@"NSString",&,V_challengeURL) challengeURL;
@property (T@"NSString",&,V_finalizeOrderURL) finalizeOrderURL;
@property (T@"NSString",&,V_orderURL) orderURL;
@property (T@"NSString",&,V_certificateURL) certificateURL;
@property (T@"NSString",&,V_nextMessageURL) nextMessageURL;
@property (T@"NSString",&,V_acmeNewAccountURL) acmeNewAccountURL;
@property (T@"NSString",&,V_acmeNewNonceURL) acmeNewNonceURL;
@property (T@"NSString",&,V_acmeNewOrderURL) acmeNewOrderURL;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpc_queue) xpc_queue;
@property (T@"NSObject<OS_xpc_object>",&,V_connection) connection;
@property (T@"SecJWSEncoder",&,V_encoder) encoder;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_publicKey) publicKey;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_privateKey) privateKey;
@property (T^{__SecCertificate=},V_certificate) certificate;
@property (T^{__SecIdentity=},V_identity) identity;
```

## Instance methods

```
-[AcmeCertRequest setSubject:];
-[AcmeCertRequest nonce];
-[AcmeCertRequest setEncoder:];
-[AcmeCertRequest authorizationURL];
-[AcmeCertRequest setAccount:];
-[AcmeCertRequest publicKey];
-[AcmeCertRequest setTimestamp:];
-[AcmeCertRequest parameters];
-[AcmeCertRequest setState:];
-[AcmeCertRequest subject];
-[AcmeCertRequest account];
-[AcmeCertRequest setPublicKey:];
-[AcmeCertRequest setParameters:];
-[AcmeCertRequest location];
-[AcmeCertRequest dealloc];
-[AcmeCertRequest timestamp];
-[AcmeCertRequest queue];
-[AcmeCertRequest serialNumber];
-[AcmeCertRequest setIdentity:];
-[AcmeCertRequest setLocation:];
-[AcmeCertRequest executeRequest];
-[AcmeCertRequest connection];
-[AcmeCertRequest identity];
-[AcmeCertRequest setConnection:];
-[AcmeCertRequest token];
-[AcmeCertRequest setToken:];
-[AcmeCertRequest certificate];
-[AcmeCertRequest state];
-[AcmeCertRequest setQueue:];
-[AcmeCertRequest acmeNewOrderURL];
-[AcmeCertRequest attestationOids];
-[AcmeCertRequest csr];
-[AcmeCertRequest encoder];
-[AcmeCertRequest setAttestation:];
-[AcmeCertRequest setCertificate:];
-[AcmeCertRequest setCsr:];
-[AcmeCertRequest acmeNewNonceURL];
-[AcmeCertRequest sanitizeSubject];
-[AcmeCertRequest acmeNewAccountURL];
-[AcmeCertRequest acmeRequest];
-[AcmeCertRequest attestation];
-[AcmeCertRequest attestationCRChain];
-[AcmeCertRequest attestationCRKey];
-[AcmeCertRequest attestationChain];
-[AcmeCertRequest attestationChainPEMRepresentation];
-[AcmeCertRequest attestationObjectWithCertificates:];
-[AcmeCertRequest authorizations];
-[AcmeCertRequest certificateURL];
-[AcmeCertRequest challengeURL];
-[AcmeCertRequest createCSR];
-[AcmeCertRequest createCertificate];
-[AcmeCertRequest createKeyPair];
-[AcmeCertRequest deviceAttestationSupported];
-[AcmeCertRequest errorStatusWithHTTPErrorCode:];
-[AcmeCertRequest finalizeOrderURL];
-[AcmeCertRequest hardwareAttestationWithError:];
-[AcmeCertRequest identityWithError:];
-[AcmeCertRequest initWithSubject:parameters:];
-[AcmeCertRequest keyParams];
-[AcmeCertRequest logAcmeCSR];
-[AcmeCertRequest nextMessageURL];
-[AcmeCertRequest orderURL];
-[AcmeCertRequest permitLocalIssuer];
-[AcmeCertRequest pollForStatus:until:];
-[AcmeCertRequest privateKey];
-[AcmeCertRequest processReply:];
-[AcmeCertRequest requestAttestationChainWithError:];
-[AcmeCertRequest requireAttestation];
-[AcmeCertRequest sanitizeParameters];
-[AcmeCertRequest sendRequestToXPCService:response:];
-[AcmeCertRequest setAcmeNewAccountURL:];
-[AcmeCertRequest setAcmeNewNonceURL:];
-[AcmeCertRequest setAcmeNewOrderURL:];
-[AcmeCertRequest setAttestationCRChain:];
-[AcmeCertRequest setAttestationCRKey:];
-[AcmeCertRequest setAttestationChain:];
-[AcmeCertRequest setAttestationOids:];
-[AcmeCertRequest setAuthorizationURL:];
-[AcmeCertRequest setAuthorizations:];
-[AcmeCertRequest setCertificateURL:];
-[AcmeCertRequest setChallengeURL:];
-[AcmeCertRequest setFinalizeOrderURL:];
-[AcmeCertRequest setKeyParams:];
-[AcmeCertRequest setLogAcmeCSR:];
-[AcmeCertRequest setNextMessageURL:];
-[AcmeCertRequest setNonce:];
-[AcmeCertRequest setOrderURL:];
-[AcmeCertRequest setPermitLocalIssuer:];
-[AcmeCertRequest setPrivateKey:];
-[AcmeCertRequest setRequireAttestation:];
-[AcmeCertRequest setXpc_queue:];
-[AcmeCertRequest valueForBooleanDefault:];
-[AcmeCertRequest xpc_queue];
```
