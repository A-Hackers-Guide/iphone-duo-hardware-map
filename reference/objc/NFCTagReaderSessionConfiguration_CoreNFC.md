# `NFCTagReaderSessionConfiguration`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _polling;
@"NSArray" _iso7816SelectIdentifiers;
@"NSArray" _felicaSystemCodes;
```

## Properties

```
@property (Tq,N,V_polling) polling;
@property (T@"NSArray",&,N,V_iso7816SelectIdentifiers) iso7816SelectIdentifiers;
@property (T@"NSArray",&,N,V_felicaSystemCodes) felicaSystemCodes;
```

## Instance methods

```
-[NFCTagReaderSessionConfiguration felicaSystemCodes];
-[NFCTagReaderSessionConfiguration iso7816SelectIdentifiers];
-[NFCTagReaderSessionConfiguration setFelicaSystemCodes:];
-[NFCTagReaderSessionConfiguration setIso7816SelectIdentifiers:];
-[NFCTagReaderSessionConfiguration polling];
-[NFCTagReaderSessionConfiguration encodeToPollConfig];
-[NFCTagReaderSessionConfiguration initWithPollingOption:iso7816SelectIdentifiers:felicaSystemCodes:];
-[NFCTagReaderSessionConfiguration setPolling:];
```
