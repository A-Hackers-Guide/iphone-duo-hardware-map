# `UIPhotoSearchSuggestion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputSuggestion`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _whoValues;
@"NSArray" _whatValues;
@"NSArray" _whereValues;
@"NSArray" _whenValues;
@"NSString" _actionText;
```

## Properties

```
@property (T@"NSString",C,N,V_actionText) actionText;
@property (T@"NSArray",C,N,V_whoValues) whoValues;
@property (T@"NSArray",C,N,V_whatValues) whatValues;
@property (T@"NSArray",C,N,V_whereValues) whereValues;
@property (T@"NSArray",C,N,V_whenValues) whenValues;
```

## Instance methods

```
-[UIPhotoSearchSuggestion initWithCandidate:];
-[UIPhotoSearchSuggestion setWhereValues:];
-[UIPhotoSearchSuggestion initWithActionText:whoValues:whatValues:whereValues:whenValues:];
-[UIPhotoSearchSuggestion photosQueryData];
-[UIPhotoSearchSuggestion actionText];
-[UIPhotoSearchSuggestion appendValues:toAttributedString:withTokenCreator:];
-[UIPhotoSearchSuggestion photosQueryRepresentation];
-[UIPhotoSearchSuggestion setActionText:];
-[UIPhotoSearchSuggestion setWhatValues:];
-[UIPhotoSearchSuggestion setWhenValues:];
-[UIPhotoSearchSuggestion setWhoValues:];
-[UIPhotoSearchSuggestion whatValues];
-[UIPhotoSearchSuggestion whenValues];
-[UIPhotoSearchSuggestion whereValues];
-[UIPhotoSearchSuggestion whoValues];
```
