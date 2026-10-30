# `SBSAInterfaceElementPropertyIdentity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSAInterfaceElementPropertyIdentifying`
- 2 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _associatedInterfaceElementIdentifier;
@"NSString" _interfaceElementProperty;
```

## Properties

```
@property (TB,R,N,GisBoundsProperty) boundsProperty;
@property (TB,R,N,GisContentBoundsProperty) contentBoundsProperty;
@property (T@"NSUUID",R,C,N,V_associatedInterfaceElementIdentifier) associatedInterfaceElementIdentifier;
@property (T@"NSString",R,C,N,V_interfaceElementProperty) interfaceElementProperty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSAInterfaceElementPropertyIdentity hash];
-[SBSAInterfaceElementPropertyIdentity description];
-[SBSAInterfaceElementPropertyIdentity copyWithZone:];
-[SBSAInterfaceElementPropertyIdentity isEqual:];
-[SBSAInterfaceElementPropertyIdentity associatedInterfaceElementIdentifier];
-[SBSAInterfaceElementPropertyIdentity initWithAssociatedInterfaceElementIdentifier:andProperty:];
-[SBSAInterfaceElementPropertyIdentity interfaceElementProperty];
-[SBSAInterfaceElementPropertyIdentity isBoundsProperty];
-[SBSAInterfaceElementPropertyIdentity isContentBoundsProperty];
```
