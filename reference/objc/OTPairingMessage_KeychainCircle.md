# `OTPairingMessage`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 7 instance variables, 12 properties, 28 instance methods, 0 class methods

## Instance variables

```
Q _version;
@"OTSponsorToApplicantRound1M2" _epoch;
@"OTApplicantToSponsorRound2M1" _prepare;
@"OTSupportOctagonMessage" _supportsOctagon;
@"OTSupportSOSMessage" _supportsSOS;
@"OTSponsorToApplicantRound2M2" _voucher;
{?="version"b1} _has;
```

## Properties

```
@property (TB,R,N) hasEpoch;
@property (T@"OTSponsorToApplicantRound1M2",&,N,V_epoch) epoch;
@property (TB,R,N) hasPrepare;
@property (T@"OTApplicantToSponsorRound2M1",&,N,V_prepare) prepare;
@property (TB,R,N) hasVoucher;
@property (T@"OTSponsorToApplicantRound2M2",&,N,V_voucher) voucher;
@property (TB,R,N) hasSupportsOctagon;
@property (T@"OTSupportOctagonMessage",&,N,V_supportsOctagon) supportsOctagon;
@property (TB,R,N) hasSupportsSOS;
@property (T@"OTSupportSOSMessage",&,N,V_supportsSOS) supportsSOS;
@property (TB,N) hasVersion;
@property (TQ,N,V_version) version;
```

## Instance methods

```
-[OTPairingMessage epoch];
-[OTPairingMessage hasVersion];
-[OTPairingMessage writeTo:];
-[OTPairingMessage setEpoch:];
-[OTPairingMessage mergeFrom:];
-[OTPairingMessage setHasVersion:];
-[OTPairingMessage version];
-[OTPairingMessage prepare];
-[OTPairingMessage hash];
-[OTPairingMessage copyTo:];
-[OTPairingMessage description];
-[OTPairingMessage setVersion:];
-[OTPairingMessage readFrom:];
-[OTPairingMessage setVoucher:];
-[OTPairingMessage voucher];
-[OTPairingMessage copyWithZone:];
-[OTPairingMessage isEqual:];
-[OTPairingMessage dictionaryRepresentation];
-[OTPairingMessage setSupportsSOS:];
-[OTPairingMessage supportsOctagon];
-[OTPairingMessage hasEpoch];
-[OTPairingMessage hasPrepare];
-[OTPairingMessage hasSupportsOctagon];
-[OTPairingMessage hasSupportsSOS];
-[OTPairingMessage hasVoucher];
-[OTPairingMessage setPrepare:];
-[OTPairingMessage setSupportsOctagon:];
-[OTPairingMessage supportsSOS];
```
