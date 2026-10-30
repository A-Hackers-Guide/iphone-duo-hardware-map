# `TCSmartActionMetadataGLPSearch`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TCSmartActionMetadata`
- 2 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _containsSensitiveData;
@"NSArray" _attributedResults;
```

## Properties

```
@property (T@"NSString",R,C,N) actionText;
@property (T@"NSArray",R,C,N,V_attributedResults) attributedResults;
@property (T@"NSArray",R,C,N) searchResults;
@property (TB,R,N,V_containsSensitiveData) containsSensitiveData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TCSmartActionMetadataGLPSearch supportsSecureCoding];
```

## Instance methods

```
-[TCSmartActionMetadataGLPSearch containsSensitiveData];
-[TCSmartActionMetadataGLPSearch searchResults];
-[TCSmartActionMetadataGLPSearch init];
-[TCSmartActionMetadataGLPSearch actionType];
-[TCSmartActionMetadataGLPSearch encodeWithCoder:];
-[TCSmartActionMetadataGLPSearch hash];
-[TCSmartActionMetadataGLPSearch initWithCoder:];
-[TCSmartActionMetadataGLPSearch copyWithZone:];
-[TCSmartActionMetadataGLPSearch isEqual:];
-[TCSmartActionMetadataGLPSearch actionText];
-[TCSmartActionMetadataGLPSearch attributedResults];
-[TCSmartActionMetadataGLPSearch initWithActionText:attributedResults:containsSensitiveData:];
```
