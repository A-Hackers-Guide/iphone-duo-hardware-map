# `FBSInvocation`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 8 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _protocolName;
@"NSString" _selectorName;
@"NSString" _encoding;
@"BSXPCCoder" _context;
@"BSMutableSettings" _objects;
@"BSAtomicSignal" _invoked;
@? _reply;
B _resolved;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSInvocation initialize];
```

## Instance methods

```
-[FBSInvocation selector];
-[FBSInvocation debugDescription];
-[FBSInvocation dealloc];
-[FBSInvocation selectorName];
-[FBSInvocation decodeWithCoder:];
-[FBSInvocation encodeWithCoder:];
-[FBSInvocation description];
-[FBSInvocation extension];
-[FBSInvocation context];
-[FBSInvocation resolve];
-[FBSInvocation membersForCoder];
-[FBSInvocation invoked];
-[FBSInvocation cannotResolveForReason:];
-[FBSInvocation compatibleWithTarget:];
-[FBSInvocation invokeWithReceiver:replyHandler:];
-[FBSInvocation invokeWithTarget:replyHandler:];
```
