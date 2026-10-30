# `SBFPhysicalButtonTarget`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 4 instance variables, 8 properties, 9 instance methods, 2 class methods

## Instance variables

```
Q _button;
Q _generation;
@"BSAuditToken" _auditToken;
Q _identifier;
```

## Properties

```
@property (TQ,R,N,V_button) button;
@property (TQ,R,N,V_generation) generation;
@property (T@"BSAuditToken",R,N,V_auditToken) auditToken;
@property (TQ,R,N,V_identifier) identifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFPhysicalButtonTarget targetWithPhysicalButton:generation:auditToken:];
+[SBFPhysicalButtonTarget targetWithPhysicalButton:generation:auditToken:identifier:];
```

## Instance methods

```
-[SBFPhysicalButtonTarget identifier];
-[SBFPhysicalButtonTarget button];
-[SBFPhysicalButtonTarget generation];
-[SBFPhysicalButtonTarget hash];
-[SBFPhysicalButtonTarget description];
-[SBFPhysicalButtonTarget appendDescriptionToStream:];
-[SBFPhysicalButtonTarget auditToken];
-[SBFPhysicalButtonTarget copyWithZone:];
-[SBFPhysicalButtonTarget isEqual:];
```
