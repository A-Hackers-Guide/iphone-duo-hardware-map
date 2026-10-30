# `NFReaderSessionInterface` (protocol)

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NFSessionInterface`
- 0 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance methods

```
-[NFReaderSessionInterface checkNdefSupportWithCompletion:];
-[NFReaderSessionInterface checkPresenceWithCompletion:];
-[NFReaderSessionInterface connect:completion:];
-[NFReaderSessionInterface disconnectWithCardRemoval:completion:];
-[NFReaderSessionInterface endSessionWithReason:completion:];
-[NFReaderSessionInterface ndefReadWithCompletion:];
-[NFReaderSessionInterface ndefWrite:completion:];
-[NFReaderSessionInterface performVAS:completion:];
-[NFReaderSessionInterface restartPollingWithConfiguration:completion:];
-[NFReaderSessionInterface setECPPayload:completion:];
-[NFReaderSessionInterface startPollingWithConfig:completion:];
-[NFReaderSessionInterface stopPollingWithCompletion:];
-[NFReaderSessionInterface transceive:completion:];
-[NFReaderSessionInterface updateSharingUIScanText:completion:];
-[NFReaderSessionInterface updateSharingUIStateOnInvalidation:completion:];
-[NFReaderSessionInterface writeProtectNDEFTagWithCompletion:];
```
