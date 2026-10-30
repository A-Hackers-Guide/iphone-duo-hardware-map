# `SBSAContainerStaticTouchAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAActionRepresenting`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _reasons;
@"NSUUID" _associatedInterfaceElementIdentifier;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_associatedInterfaceElementIdentifier) associatedInterfaceElementIdentifier;
@property (T@"NSArray",R,C,N,V_reasons) reasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAContainerStaticTouchAction initialize];
```

## Instance methods

```
-[SBSAContainerStaticTouchAction reasons];
-[SBSAContainerStaticTouchAction encodeWithCoder:];
-[SBSAContainerStaticTouchAction hash];
-[SBSAContainerStaticTouchAction description];
-[SBSAContainerStaticTouchAction copyWithZone:];
-[SBSAContainerStaticTouchAction isEqual:];
-[SBSAContainerStaticTouchAction membersForCoder];
-[SBSAContainerStaticTouchAction associatedInterfaceElementIdentifier];
-[SBSAContainerStaticTouchAction initWithAssociatedInterfaceElementIdentifier:reasons:];
```
