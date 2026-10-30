# `SBSAContainerResizeAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAActionRepresenting`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _reasons;
q _resizeActionResult;
@"NSUUID" _associatedInterfaceElementIdentifier;
```

## Properties

```
@property (Tq,R,N,V_resizeActionResult) resizeActionResult;
@property (T@"NSUUID",R,C,N,V_associatedInterfaceElementIdentifier) associatedInterfaceElementIdentifier;
@property (T@"NSArray",R,C,N,V_reasons) reasons;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAContainerResizeAction initialize];
```

## Instance methods

```
-[SBSAContainerResizeAction reasons];
-[SBSAContainerResizeAction encodeWithCoder:];
-[SBSAContainerResizeAction hash];
-[SBSAContainerResizeAction description];
-[SBSAContainerResizeAction copyWithZone:];
-[SBSAContainerResizeAction isEqual:];
-[SBSAContainerResizeAction membersForCoder];
-[SBSAContainerResizeAction associatedInterfaceElementIdentifier];
-[SBSAContainerResizeAction initWithResult:associatedInterfaceElementIdentifier:reasons:];
-[SBSAContainerResizeAction resizeActionResult];
```
