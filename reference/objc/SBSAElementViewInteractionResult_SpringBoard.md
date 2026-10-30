# `SBSAElementViewInteractionResult`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `SAElementIdentifying`, `SBSABlockMutating`
- 4 instance variables, 8 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
Q _interactionSource;
q _viewInteractionResult;
```

## Properties

```
@property (T@"NSString",C,N,S_setClientIdentifier:,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,S_setElementIdentifier:,V_elementIdentifier) elementIdentifier;
@property (TQ,N,S_setInteractionSource:,V_interactionSource) interactionSource;
@property (Tq,N,S_setViewInteractionResult:,V_viewInteractionResult) viewInteractionResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAElementViewInteractionResult instanceWithBlock:];
+[SBSAElementViewInteractionResult mutatorClass];
```

## Instance methods

```
-[SBSAElementViewInteractionResult clientIdentifier];
-[SBSAElementViewInteractionResult elementIdentifier];
-[SBSAElementViewInteractionResult interactionSource];
-[SBSAElementViewInteractionResult hash];
-[SBSAElementViewInteractionResult description];
-[SBSAElementViewInteractionResult copyWithZone:];
-[SBSAElementViewInteractionResult isEqual:];
-[SBSAElementViewInteractionResult copyWithBlock:];
-[SBSAElementViewInteractionResult _setClientIdentifier:];
-[SBSAElementViewInteractionResult _setElementIdentifier:];
-[SBSAElementViewInteractionResult _setInteractionSource:];
-[SBSAElementViewInteractionResult _setViewInteractionResult:];
-[SBSAElementViewInteractionResult initWithIdentity:interactionSource:viewInteractionResult:];
-[SBSAElementViewInteractionResult viewInteractionResult];
```
