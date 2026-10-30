# `TCTokenDifferenceManager`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _input;
@"NSString" _output;
@"NSArray" _inputTokens;
@"NSArray" _outputTokens;
@"NSArray" _tokenEdits;
@"NSArray" _tokenDifferences;
@"NSDictionary" _tokenToTokenIdMap;
@"NSDictionary" _tokenIdToTokenMap;
```

## Properties

```
@property (T@"NSString",R,C,V_input) input;
@property (T@"NSString",R,C,V_output) output;
@property (T@"NSArray",R,C,V_inputTokens) inputTokens;
@property (T@"NSArray",R,C,V_outputTokens) outputTokens;
@property (T@"NSArray",R,C,V_tokenEdits) tokenEdits;
@property (T@"NSArray",R,C,V_tokenDifferences) tokenDifferences;
@property (T@"NSDictionary",R,C,V_tokenToTokenIdMap) tokenToTokenIdMap;
@property (T@"NSDictionary",R,C,V_tokenIdToTokenMap) tokenIdToTokenMap;
```

## Instance methods

```
-[TCTokenDifferenceManager input];
-[TCTokenDifferenceManager output];
-[TCTokenDifferenceManager inputTokens];
-[TCTokenDifferenceManager initWithInput:output:];
-[TCTokenDifferenceManager _tokensForString:tagger:tokenToTokenIdMap:];
-[TCTokenDifferenceManager initWithInput:output:tagger:];
-[TCTokenDifferenceManager outputTokens];
-[TCTokenDifferenceManager tokenDifferences];
-[TCTokenDifferenceManager tokenEdits];
-[TCTokenDifferenceManager tokenIdToTokenMap];
-[TCTokenDifferenceManager tokenToTokenIdMap];
```
