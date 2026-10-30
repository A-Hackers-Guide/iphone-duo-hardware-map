# `WiFiAwarePublishDatapathSecurityConfiguration`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _pmkList;
@"NSArray" _passphraseList;
@"NSData" _pmkID;
@"WiFiAwarePairingConfiguration" _pairingConfiguration;
@"<WiFiAwarePublisherPairingDelegate>" _pairingDelegate;
@"NSString" _pairingPINCode;
@"NSString" _pairingPassphrase;
@"NSData" _pairingQRCodeInformation;
@"NSData" _pairingNFCTag;
@"NSString" _pinCode;
```

## Properties

```
@property (T@"NSArray",R,N,V_pmkList) pmkList;
@property (T@"NSArray",R,N,V_passphraseList) passphraseList;
@property (T@"NSData",R,N,V_pmkID) pmkID;
@property (T@"WiFiAwarePairingConfiguration",C,N,V_pairingConfiguration) pairingConfiguration;
@property (T@"<WiFiAwarePublisherPairingDelegate>",W,N,V_pairingDelegate) pairingDelegate;
@property (T@"NSString",R,N,V_pairingPINCode) pairingPINCode;
@property (T@"NSString",R,N,V_pairingPassphrase) pairingPassphrase;
@property (T@"NSData",R,N,V_pairingQRCodeInformation) pairingQRCodeInformation;
@property (T@"NSData",R,N,V_pairingNFCTag) pairingNFCTag;
@property (T@"NSString",C,N,V_pinCode) pinCode;
```

## Class methods

```
+[WiFiAwarePublishDatapathSecurityConfiguration supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublishDatapathSecurityConfiguration encodeWithCoder:];
-[WiFiAwarePublishDatapathSecurityConfiguration description];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithCoder:];
-[WiFiAwarePublishDatapathSecurityConfiguration isEqual:];
-[WiFiAwarePublishDatapathSecurityConfiguration pinCode];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:];
-[WiFiAwarePublishDatapathSecurityConfiguration setPairingDelegate:];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingDelegate];
-[WiFiAwarePublishDatapathSecurityConfiguration setPinCode:];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingConfiguration];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPMKList:passphraseList:];
-[WiFiAwarePublishDatapathSecurityConfiguration pmkList];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPMK:andPMKID:];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingNFCTag:];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingPINCode:];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingPassphrase:];
-[WiFiAwarePublishDatapathSecurityConfiguration initWithPairingConfiguration:usingPairingDelegate:usingPairingQRCodeInformation:];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingNFCTag];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingPINCode];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingPassphrase];
-[WiFiAwarePublishDatapathSecurityConfiguration pairingQRCodeInformation];
-[WiFiAwarePublishDatapathSecurityConfiguration passphraseList];
-[WiFiAwarePublishDatapathSecurityConfiguration pmkID];
-[WiFiAwarePublishDatapathSecurityConfiguration setPairingConfiguration:];
```
