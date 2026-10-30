# `CWFWiFiNetworkSharingEAPCredentials`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 13 instance variables, 13 properties, 33 instance methods, 1 class methods

## Instance variables

```
B _TLSCertificateRequired;
B _FASTUsePAC;
B _FASTProvisionPACAnonymously;
@"NSString" _outerIdentity;
@"NSArray" _trustedServerCertificates;
@"NSArray" _trustedServerNames;
@"NSArray" _clientCertificateChain;
@"NSData" _clientPrivateKey;
@"NSString" _username;
@"NSSet" _acceptedEAPTypes;
@"NSString" _TLSMinimumVersion;
@"NSString" _TLSMaximumVersion;
q _TTLSInnerAuthenticationType;
```

## Properties

```
@property (T@"NSString",C,N,V_outerIdentity) outerIdentity;
@property (T@"NSArray",C,N,V_trustedServerCertificates) trustedServerCertificates;
@property (T@"NSArray",C,N,V_trustedServerNames) trustedServerNames;
@property (T@"NSArray",C,N,V_clientCertificateChain) clientCertificateChain;
@property (T@"NSData",C,N,V_clientPrivateKey) clientPrivateKey;
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSSet",C,N,V_acceptedEAPTypes) acceptedEAPTypes;
@property (T@"NSString",C,N,V_TLSMinimumVersion) TLSMinimumVersion;
@property (T@"NSString",C,N,V_TLSMaximumVersion) TLSMaximumVersion;
@property (TB,N,V_TLSCertificateRequired) TLSCertificateRequired;
@property (Tq,N,V_TTLSInnerAuthenticationType) TTLSInnerAuthenticationType;
@property (TB,N,V_FASTUsePAC) FASTUsePAC;
@property (TB,N,V_FASTProvisionPACAnonymously) FASTProvisionPACAnonymously;
```

## Class methods

```
+[CWFWiFiNetworkSharingEAPCredentials supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingEAPCredentials username];
-[CWFWiFiNetworkSharingEAPCredentials encodeWithCoder:];
-[CWFWiFiNetworkSharingEAPCredentials description];
-[CWFWiFiNetworkSharingEAPCredentials initWithCoder:];
-[CWFWiFiNetworkSharingEAPCredentials setUsername:];
-[CWFWiFiNetworkSharingEAPCredentials copyWithZone:];
-[CWFWiFiNetworkSharingEAPCredentials outerIdentity];
-[CWFWiFiNetworkSharingEAPCredentials setOuterIdentity:];
-[CWFWiFiNetworkSharingEAPCredentials setTrustedServerCertificates:];
-[CWFWiFiNetworkSharingEAPCredentials setTrustedServerNames:];
-[CWFWiFiNetworkSharingEAPCredentials trustedServerNames];
-[CWFWiFiNetworkSharingEAPCredentials FASTProvisionPACAnonymously];
-[CWFWiFiNetworkSharingEAPCredentials setFASTProvisionPACAnonymously:];
-[CWFWiFiNetworkSharingEAPCredentials FASTUsePAC];
-[CWFWiFiNetworkSharingEAPCredentials setTTLSInnerAuthenticationType:];
-[CWFWiFiNetworkSharingEAPCredentials TLSCertificateRequired];
-[CWFWiFiNetworkSharingEAPCredentials TLSMaximumVersion];
-[CWFWiFiNetworkSharingEAPCredentials TLSMinimumVersion];
-[CWFWiFiNetworkSharingEAPCredentials TTLSInnerAuthenticationType];
-[CWFWiFiNetworkSharingEAPCredentials __TTLSInnerAuthenticationTypeForString:];
-[CWFWiFiNetworkSharingEAPCredentials __acceptedCWFWiFiNetworkSharingEAPTypes:];
-[CWFWiFiNetworkSharingEAPCredentials acceptedEAPTypes];
-[CWFWiFiNetworkSharingEAPCredentials clientCertificateChain];
-[CWFWiFiNetworkSharingEAPCredentials clientPrivateKey];
-[CWFWiFiNetworkSharingEAPCredentials initWithShareableEAPConfiguration:];
-[CWFWiFiNetworkSharingEAPCredentials setAcceptedEAPTypes:];
-[CWFWiFiNetworkSharingEAPCredentials setClientCertificateChain:];
-[CWFWiFiNetworkSharingEAPCredentials setClientPrivateKey:];
-[CWFWiFiNetworkSharingEAPCredentials setFASTUsePAC:];
-[CWFWiFiNetworkSharingEAPCredentials setTLSCertificateRequired:];
-[CWFWiFiNetworkSharingEAPCredentials setTLSMaximumVersion:];
-[CWFWiFiNetworkSharingEAPCredentials setTLSMinimumVersion:];
-[CWFWiFiNetworkSharingEAPCredentials trustedServerCertificates];
```
