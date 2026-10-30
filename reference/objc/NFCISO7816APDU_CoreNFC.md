# `NFCISO7816APDU`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
{_NSRange="location"Q"length"Q} _payloadOffset;
q _le;
@"NSData" _fullPacket;
```

## Properties

```
@property (TC,R,N) instructionClass;
@property (TC,R,N) instructionCode;
@property (TC,R,N) p1Parameter;
@property (TC,R,N) p2Parameter;
@property (T@"NSData",R,C,N) data;
@property (Tq,R,N) expectedResponseLength;
```

## Instance methods

```
-[NFCISO7816APDU data];
-[NFCISO7816APDU description];
-[NFCISO7816APDU initWithData:];
-[NFCISO7816APDU copyWithZone:];
-[NFCISO7816APDU asData];
-[NFCISO7816APDU instructionCode];
-[NFCISO7816APDU expectedResponseLength];
-[NFCISO7816APDU initWithInstructionClass:instructionCode:p1Parameter:p2Parameter:data:expectedResponseLength:];
-[NFCISO7816APDU instructionClass];
-[NFCISO7816APDU p1Parameter];
-[NFCISO7816APDU p2Parameter];
```
