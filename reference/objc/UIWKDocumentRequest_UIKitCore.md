# `UIWKDocumentRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<NSCopying>" _inputElementIdentifier;
q _flags;
q _surroundingGranularity;
q _granularityCount;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _documentRect;
```

## Properties

```
@property (Tq,N,V_flags) flags;
@property (Tq,N,V_surroundingGranularity) surroundingGranularity;
@property (Tq,N,V_granularityCount) granularityCount;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_documentRect) documentRect;
@property (T@"<NSCopying>",&,N,V_inputElementIdentifier) inputElementIdentifier;
```

## Instance methods

```
-[UIWKDocumentRequest setFlags:];
-[UIWKDocumentRequest flags];
-[UIWKDocumentRequest dealloc];
-[UIWKDocumentRequest documentRect];
-[UIWKDocumentRequest granularityCount];
-[UIWKDocumentRequest inputElementIdentifier];
-[UIWKDocumentRequest setDocumentRect:];
-[UIWKDocumentRequest setGranularityCount:];
-[UIWKDocumentRequest setInputElementIdentifier:];
-[UIWKDocumentRequest setSurroundingGranularity:];
-[UIWKDocumentRequest surroundingGranularity];
```
