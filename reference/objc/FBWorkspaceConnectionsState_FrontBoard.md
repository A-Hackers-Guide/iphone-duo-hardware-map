# `FBWorkspaceConnectionsState`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 2 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSMutableIndexSet" _pidSet;
```

## Properties

```
@property (TQ,R,N) serializedDataLength;
@property (T@"NSSet",R,C,N) processIdentifiers;
```

## Class methods

```
+[FBWorkspaceConnectionsState deserializeLength:fromReader:];
+[FBWorkspaceConnectionsState minimumSerializedDataLength];
```

## Instance methods

```
-[FBWorkspaceConnectionsState mutableCopyWithZone:];
-[FBWorkspaceConnectionsState processIdentifiers];
-[FBWorkspaceConnectionsState init];
-[FBWorkspaceConnectionsState copy];
-[FBWorkspaceConnectionsState serializeToWriter:];
-[FBWorkspaceConnectionsState _initWithIndexSet:];
-[FBWorkspaceConnectionsState hash];
-[FBWorkspaceConnectionsState description];
-[FBWorkspaceConnectionsState serializedDataLength];
-[FBWorkspaceConnectionsState copyWithZone:];
-[FBWorkspaceConnectionsState isEqual:];
-[FBWorkspaceConnectionsState mutableCopy];
```
