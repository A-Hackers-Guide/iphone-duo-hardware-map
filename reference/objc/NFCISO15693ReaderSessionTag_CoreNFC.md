# `NFCISO15693ReaderSessionTag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NFCTag`
- Protocols: `NFCISO15693Tag`
- 0 instance variables, 10 properties, 39 instance methods, 2 class methods

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

## Class methods

```
+[NFCISO15693ReaderSessionTag decodeIdentifier:manufacturerCode:serialNumber:];
+[NFCISO15693ReaderSessionTag reverseByteOrder:];
```

## Instance methods

```
-[NFCISO15693ReaderSessionTag identifier];
-[NFCISO15693ReaderSessionTag copyWithZone:];
-[NFCISO15693ReaderSessionTag stayQuietWithCompletionHandler:];
-[NFCISO15693ReaderSessionTag _parseResponseData:outError:];
-[NFCISO15693ReaderSessionTag _parseResponseErrorWithData:];
-[NFCISO15693ReaderSessionTag _transceiveWithData:receivedData:commandConfig:error:];
-[NFCISO15693ReaderSessionTag authenticateWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:];
-[NFCISO15693ReaderSessionTag challengeWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:];
-[NFCISO15693ReaderSessionTag customCommandWithRequestFlag:customCommandCode:customRequestParameters:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedLockBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedReadMultipleBlocksWithRequestFlags:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedReadSingleBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:];
-[NFCISO15693ReaderSessionTag extendedWriteSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:];
-[NFCISO15693ReaderSessionTag fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag getMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag getSystemInfoAndUIDWithRequestFlag:completionHandler:];
-[NFCISO15693ReaderSessionTag getSystemInfoWithRequestFlag:completionHandler:];
-[NFCISO15693ReaderSessionTag icManufacturerCode];
-[NFCISO15693ReaderSessionTag icSerialNumber];
-[NFCISO15693ReaderSessionTag keyUpdateWithRequestFlags:keyIdentifier:message:completionHandler:];
-[NFCISO15693ReaderSessionTag lockAFIWithRequestFlag:completionHandler:];
-[NFCISO15693ReaderSessionTag lockBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693ReaderSessionTag lockDFSIDWithRequestFlag:completionHandler:];
-[NFCISO15693ReaderSessionTag lockDSFIDWithRequestFlag:completionHandler:];
-[NFCISO15693ReaderSessionTag readBufferWithRequestFlags:completionHandler:];
-[NFCISO15693ReaderSessionTag readMultipleBlocksWithConfiguration:completionHandler:];
-[NFCISO15693ReaderSessionTag readMultipleBlocksWithRequestFlags:blockRange:completionHandler:];
-[NFCISO15693ReaderSessionTag readSingleBlockWithRequestFlags:blockNumber:completionHandler:];
-[NFCISO15693ReaderSessionTag resetToReadyWithRequestFlags:completionHandler:];
-[NFCISO15693ReaderSessionTag selectWithRequestFlags:completionHandler:];
-[NFCISO15693ReaderSessionTag sendCustomCommandWithConfiguration:completionHandler:];
-[NFCISO15693ReaderSessionTag sendRequestWithFlag:commandCode:data:completionHandler:];
-[NFCISO15693ReaderSessionTag writeAFIWithRequestFlag:afi:completionHandler:];
-[NFCISO15693ReaderSessionTag writeDSFIDWithRequestFlag:dsfid:completionHandler:];
-[NFCISO15693ReaderSessionTag writeMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:];
-[NFCISO15693ReaderSessionTag writeSingleBlockWithRequestFlags:blockNumber:dataBlock:completionHandler:];
```
