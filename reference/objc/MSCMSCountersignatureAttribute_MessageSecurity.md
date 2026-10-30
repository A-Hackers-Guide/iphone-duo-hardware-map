# `MSCMSCountersignatureAttribute`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MSCMSAttributeCoder`
- 4 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"MSCMSSignerInfo" _containingSignerInfo;
@"NSArray" _signers;
Q _chainMode;
@"NSArray" _additionalCertificates;
```

## Properties

```
@property (TQ,V_chainMode) chainMode;
@property (T@"NSArray",&,V_additionalCertificates) additionalCertificates;
@property (T@"MSCMSSignerInfo",W,N,V_containingSignerInfo) containingSignerInfo;
@property (T@"NSArray",R,V_signers) signers;
@property (T@"MSOID",R,&) attributeType;
```

## Instance methods

```
-[MSCMSCountersignatureAttribute removeSignersWithIdentity:error:];
-[MSCMSCountersignatureAttribute removeSignerCertificatesWithIndexes:];
-[MSCMSCountersignatureAttribute attributeType];
-[MSCMSCountersignatureAttribute signers];
-[MSCMSCountersignatureAttribute removeSignersWithIndexes:error:];
-[MSCMSCountersignatureAttribute addSigner:];
-[MSCMSCountersignatureAttribute removeSignersWithEmailAddress:error:];
-[MSCMSCountersignatureAttribute removeSignersWithCertificate:error:];
-[MSCMSCountersignatureAttribute containingSignerInfo];
-[MSCMSCountersignatureAttribute addSigner:withChainMode:error:];
-[MSCMSCountersignatureAttribute addSigner:withCertificates:];
-[MSCMSCountersignatureAttribute setContainingSignerInfo:];
-[MSCMSCountersignatureAttribute initWithAttribute:error:];
-[MSCMSCountersignatureAttribute setAdditionalCertificates:];
-[MSCMSCountersignatureAttribute initWithAttribute:certificates:LAContext:error:];
-[MSCMSCountersignatureAttribute additionalCertificates];
-[MSCMSCountersignatureAttribute chainMode];
-[MSCMSCountersignatureAttribute encodeAttributeWithError:];
-[MSCMSCountersignatureAttribute initWithAttribute:LAContext:error:];
-[MSCMSCountersignatureAttribute initWithAttribute:certificates:LAContext:containingSignerInfo:error:];
-[MSCMSCountersignatureAttribute initWithSignerInfo:];
-[MSCMSCountersignatureAttribute initWithSignerInfo:additionalCertificates:];
-[MSCMSCountersignatureAttribute initWithSignerInfo:signerChainMode:];
-[MSCMSCountersignatureAttribute initWithSignerInfo:signerChainMode:additionalCertificates:];
-[MSCMSCountersignatureAttribute setChainMode:];
-[MSCMSCountersignatureAttribute verifyCountersignatures:error:];
-[MSCMSCountersignatureAttribute verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:signature:error:];
```
