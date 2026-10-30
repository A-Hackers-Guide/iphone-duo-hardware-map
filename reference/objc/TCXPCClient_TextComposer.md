# `TCXPCClient`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
B _valid;
```

## Instance methods

```
-[TCXPCClient init];
-[TCXPCClient setValid:];
-[TCXPCClient requestCheckingOfString:language:offset:options:completionHandler:];
-[TCXPCClient requestResultOptionsForUUIDString:completionHandler:];
-[TCXPCClient isValid];
-[TCXPCClient connection];
-[TCXPCClient _dataFromCheckingString:language:offset:optionsData:completionHandler:];
-[TCXPCClient _dataFromProofreadingReviewOfString:language:offset:optionsData:completionHandler:];
-[TCXPCClient _dataFromUUIDString:completionHandler:];
-[TCXPCClient _resultOptionsFromData:];
-[TCXPCClient _textCheckingResultsFromData:];
-[TCXPCClient recordResponse:toGrammarDetail:language:appIdentifier:];
-[TCXPCClient requestProofreadingReviewOfString:language:offset:options:completionHandler:];
```
