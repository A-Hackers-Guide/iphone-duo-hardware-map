# `SBLayoutElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLayoutElementDescriptor`, `SBWorkspaceEntityGenerating`, `BSDescriptionProviding`, `NSCopying`
- 5 instance variables, 9 properties, 18 instance methods, 2 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
q _layoutRole;
@"SBLayoutRoleSet" _supportedLayoutRoles;
Q _layoutAttributes;
@? _entityGenerator;
```

## Properties

```
@property (T@?,C,N,V_entityGenerator) entityGenerator;
@property (T@"NSString",R,C,N) uniqueIdentifier;
@property (Tq,R,N) layoutRole;
@property (T@"SBLayoutRoleSet",R,N) supportedLayoutRoles;
@property (TQ,R,N) layoutAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBLayoutElement elementWithDescriptor:];
+[SBLayoutElement elementWithDescriptor:layoutRole:];
```

## Instance methods

```
-[SBLayoutElement workspaceEntity];
-[SBLayoutElement layoutRole];
-[SBLayoutElement succinctDescriptionBuilder];
-[SBLayoutElement layoutAttributes];
-[SBLayoutElement descriptionWithMultilinePrefix:];
-[SBLayoutElement uniqueIdentifier];
-[SBLayoutElement succinctDescription];
-[SBLayoutElement initWithIdentifier:layoutRole:supportedLayoutRoles:layoutAttributes:entityGenerator:];
-[SBLayoutElement supportedLayoutRoles];
-[SBLayoutElement hash];
-[SBLayoutElement entityGenerator];
-[SBLayoutElement description];
-[SBLayoutElement hasLayoutAttributes:];
-[SBLayoutElement copyWithZone:];
-[SBLayoutElement isEqual:];
-[SBLayoutElement representsSameLayoutElementAsDescriptor:];
-[SBLayoutElement setEntityGenerator:];
-[SBLayoutElement descriptionBuilderWithMultilinePrefix:];
```
