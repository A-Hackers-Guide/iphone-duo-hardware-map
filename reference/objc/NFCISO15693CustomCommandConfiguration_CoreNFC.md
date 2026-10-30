# `NFCISO15693CustomCommandConfiguration`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTagCommandConfiguration`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
C _flags;
Q _manufacturerCode;
Q _customCommandCode;
@"NSData" _requestParameters;
```

## Properties

```
@property (TC,N,V_flags) flags;
@property (TQ,N,V_manufacturerCode) manufacturerCode;
@property (TQ,N,V_customCommandCode) customCommandCode;
@property (T@"NSData",C,N,V_requestParameters) requestParameters;
```

## Instance methods

```
-[NFCISO15693CustomCommandConfiguration requestParameters];
-[NFCISO15693CustomCommandConfiguration setRequestParameters:];
-[NFCISO15693CustomCommandConfiguration setFlags:];
-[NFCISO15693CustomCommandConfiguration flags];
-[NFCISO15693CustomCommandConfiguration copyWithZone:];
-[NFCISO15693CustomCommandConfiguration asNSDataWithError:];
-[NFCISO15693CustomCommandConfiguration customCommandCode];
-[NFCISO15693CustomCommandConfiguration initWithManufacturerCode:customCommandCode:requestParameters:];
-[NFCISO15693CustomCommandConfiguration initWithManufacturerCode:customCommandCode:requestParameters:maximumRetries:retryInterval:];
-[NFCISO15693CustomCommandConfiguration manufacturerCode];
-[NFCISO15693CustomCommandConfiguration setCustomCommandCode:];
-[NFCISO15693CustomCommandConfiguration setManufacturerCode:];
```
