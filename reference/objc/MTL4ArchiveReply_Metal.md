# `MTL4ArchiveReply`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSString" _errorMessage;
Q _type;
@"NSObject<OS_dispatch_data>" _binary;
@"NSObject<OS_dispatch_data>" _reflectionBlock;
@"NSObject<OS_dispatch_data>" _airScript;
```

## Properties

```
@property (T@"NSString",R,C) errorMessage;
@property (T@"NSObject<OS_dispatch_data>",R,N,V_binary) binary;
@property (T@"NSObject<OS_dispatch_data>",R,N,V_reflectionBlock) reflectionBlock;
@property (T@"NSObject<OS_dispatch_data>",R,N,V_airScript) airScript;
@property (TQ,R,V_type) type;
@property (TB,R) isError;
```

## Instance methods

```
-[MTL4ArchiveReply airScript];
-[MTL4ArchiveReply dealloc];
-[MTL4ArchiveReply initWithError:];
-[MTL4ArchiveReply type];
-[MTL4ArchiveReply reflectionBlock];
-[MTL4ArchiveReply errorMessage];
-[MTL4ArchiveReply isError];
-[MTL4ArchiveReply binary];
-[MTL4ArchiveReply initWithData:reflectionBlock:airScript:];
-[MTL4ArchiveReply setTypeInternal:];
```
