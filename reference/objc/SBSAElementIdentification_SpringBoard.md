# `SBSAElementIdentification`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SAElementIdentifying`, `NSCopying`
- 2 instance variables, 6 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",R,C,N,V_elementIdentifier) elementIdentifier;
```

## Class methods

```
+[SBSAElementIdentification initialize];
```

## Instance methods

```
-[SBSAElementIdentification clientIdentifier];
-[SBSAElementIdentification elementIdentifier];
-[SBSAElementIdentification hash];
-[SBSAElementIdentification description];
-[SBSAElementIdentification copyWithZone:];
-[SBSAElementIdentification isEqual:];
-[SBSAElementIdentification membersForCoder];
-[SBSAElementIdentification initWithClientIdentifier:elementIdentifier:];
-[SBSAElementIdentification initWithElementIdentification:];
```
