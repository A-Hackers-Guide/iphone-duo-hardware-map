# `TCTextServer`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCXPCTextServer`
- 0 instance variables, 0 properties, 15 instance methods, 3 class methods

## Class methods

```
+[TCTextServer validatedDetailDictionaryForDictionary:];
+[TCTextServer validatedOptionsDictionaryForDictionary:];
+[TCTextServer validatedOptionsDictionaryForOptionsData:editorTypes:];
```

## Instance methods

```
-[TCTextServer _checkString:language:offset:options:completionHandler:];
-[TCTextServer _reviewString:language:offset:options:completionHandler:];
-[TCTextServer _timeoutQueue];
-[TCTextServer _xpc_batchDataFromTokenVectorEmbeddingForStrings:language:identifier:completionHandler:];
-[TCTextServer _xpc_compileEmbeddingForIdentifier:completionHandler:];
-[TCTextServer _xpc_compiledEmbeddingModelCacheForIdentifier:completionHandler:];
-[TCTextServer _xpc_dataFromCheckingGrammarInString:language:offset:optionsData:completionHandler:];
-[TCTextServer _xpc_dataFromCheckingString:language:offset:optionsData:completionHandler:];
-[TCTextServer _xpc_dataFromProofreadingReviewOfString:language:offset:optionsData:completionHandler:];
-[TCTextServer _xpc_dataFromResultOptionsForUUIDString:completionHandler:];
-[TCTextServer _xpc_dataFromSentenceVectorEmbeddingForString:language:identifier:completionHandler:];
-[TCTextServer _xpc_dataFromTokenVectorEmbeddingForString:language:identifier:completionHandler:];
-[TCTextServer _xpc_loadTokenVectorEmbeddingForIdentifier:timeout:completionHandler:];
-[TCTextServer _xpc_recordResponse:toGrammarDetailPropertyListData:language:appIdentifier:];
-[TCTextServer prewarmEditor];
```
