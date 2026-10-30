# `NFCPaymentTagReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTagReaderSession`
- 0 instance variables, 0 properties, 6 instance methods, 2 class methods

## Class methods

```
+[NFCPaymentTagReaderSession readingAvailable];
+[NFCPaymentTagReaderSession isPaymentSession];
```

## Instance methods

```
-[NFCPaymentTagReaderSession initWithDelegate:queue:];
-[NFCPaymentTagReaderSession initWithConfiguration:delegate:queue:];
-[NFCPaymentTagReaderSession initWithDelegate:sessionDelegateType:sessionType:pollConfig:queue:];
-[NFCPaymentTagReaderSession initWithPollConfig:swiftDelegate:sessionType:queue:];
-[NFCPaymentTagReaderSession initWithPollingOption:delegate:queue:];
-[NFCPaymentTagReaderSession initWithSwiftDelegate:queue:];
```
