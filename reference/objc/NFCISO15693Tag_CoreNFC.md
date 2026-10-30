# `NFCISO15693Tag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTag`
- Protocols: `NFCISO15693Tag`
- 0 instance variables, 10 properties, 39 instance methods, 0 class methods

## Properties

```
@property (T@"NSData",R,C,N) identifier;
@property (TQ,R,N) icManufacturerCode;
@property (T@"NSData",R,C,N) icSerialNumber;
@property (TQ,R,N) type;
@property (T@"<NFCReaderSession>",R,W,N) session;
@property (TB,R,N,GisAvailable) available;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NFCISO15693Tag identifier];
-[NFCISO15693Tag copyWithZone:];
-[NFCISO15693Tag stayQuietWithCompletionHandler:];
-[NFCISO15693Tag _generateRequestHeader:flags:];
-[NFCISO15693Tag _parseResponseErrorWithData:];
-[NFCISO15693Tag _wtxRetryWithCommnand:maxRetry:completionHandler:];
-[NFCISO15693Tag authenticateWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:];
-[NFCISO15693Tag challengeWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:];
-[NFCISO15693Tag customCommandWithRequestFlag:customCommandCode:customRequestParameters:completionHandler:];
-[NFCISO15693Tag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693Tag extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693Tag extendedLockBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693Tag extendedReadMultipleBlocksWithRequestFlags:blockRange:completionHandler:];
-[NFCISO15693Tag extendedReadSingleBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693Tag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:];
-[NFCISO15693Tag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:];
-[NFCISO15693Tag fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693Tag getMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693Tag getSystemInfoAndUIDWithRequestFlag:completionHandler:];
-[NFCISO15693Tag getSystemInfoWithRequestFlag:completionHandler:];
-[NFCISO15693Tag icManufacturerCode];
-[NFCISO15693Tag icSerialNumber];
-[NFCISO15693Tag keyUpdateWithRequestFlags:keyIdentifier:message:completionHandler:];
-[NFCISO15693Tag lockAFIWithRequestFlag:completionHandler:];
-[NFCISO15693Tag lockBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693Tag lockDFSIDWithRequestFlag:completionHandler:];
-[NFCISO15693Tag lockDSFIDWithRequestFlag:completionHandler:];
-[NFCISO15693Tag readBufferWithRequestFlags:completionHandler:];
-[NFCISO15693Tag readMultipleBlocksWithConfiguration:completionHandler:];
-[NFCISO15693Tag readMultipleBlocksWithRequestFlags:blockRange:completionHandler:];
-[NFCISO15693Tag readSingleBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693Tag resetToReadyWithRequestFlags:completionHandler:];
-[NFCISO15693Tag selectWithRequestFlags:completionHandler:];
-[NFCISO15693Tag sendCustomCommandWithConfiguration:completionHandler:];
-[NFCISO15693Tag sendRequestWithFlag:commandCode:data:completionHandler:];
-[NFCISO15693Tag writeAFIWithRequestFlag:afi:completionHandler:];
-[NFCISO15693Tag writeDSFIDWithRequestFlag:dsfid:completionHandler:];
-[NFCISO15693Tag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:];
-[NFCISO15693Tag writeSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:];
```
