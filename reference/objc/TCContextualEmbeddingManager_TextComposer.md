# `TCContextualEmbeddingManager`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NLContextualEmbedding" _currentEmbedding;
@"NSMutableDictionary" _compileCacheForIdentifier;
```

## Class methods

```
+[TCContextualEmbeddingManager sharedManager];
```

## Instance methods

```
-[TCContextualEmbeddingManager batchDataFromTokenVectorEmbeddingForStrings:language:identifier:tokenDictionaries:error:];
-[TCContextualEmbeddingManager compileEmbeddingForIdentifier:cachePath:error:];
-[TCContextualEmbeddingManager compileEmbeddingForIdentifier:error:];
-[TCContextualEmbeddingManager contextualEmbeddingWithIdentifier:];
-[TCContextualEmbeddingManager dataFromSentenceVectorEmbeddingForString:language:identifier:error:];
-[TCContextualEmbeddingManager dataFromTokenVectorEmbeddingForString:language:identifier:tokenDictionaries:error:];
-[TCContextualEmbeddingManager enableE5];
-[TCContextualEmbeddingManager loadTokenVectorEmbeddingForIdentifier:error:];
-[TCContextualEmbeddingManager shouldAbortCompileEmbeddingForIdentifier:];
```
