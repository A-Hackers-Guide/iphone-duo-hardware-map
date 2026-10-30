# `SBLayoutElementDescriptor` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C,N) uniqueIdentifier;
@property (Tq,R,N) layoutRole;
@property (T@"SBLayoutRoleSet",R,N) supportedLayoutRoles;
@property (TQ,R,N) layoutAttributes;
@property (T@?,R,C,N) entityGenerator;
```

## Instance methods

```
-[SBLayoutElementDescriptor layoutRole];
-[SBLayoutElementDescriptor layoutAttributes];
-[SBLayoutElementDescriptor uniqueIdentifier];
-[SBLayoutElementDescriptor supportedLayoutRoles];
-[SBLayoutElementDescriptor entityGenerator];
-[SBLayoutElementDescriptor hasLayoutAttributes:];
-[SBLayoutElementDescriptor representsSameLayoutElementAsDescriptor:];
```
