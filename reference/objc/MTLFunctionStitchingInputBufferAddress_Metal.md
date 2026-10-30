# `MTLFunctionStitchingInputBufferAddress`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLFunctionStitchingInputNodeSPI`
- 3 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _dereference;
Q _bindIndex;
Q _byteOffset;
```

## Properties

```
@property (TQ,N,V_byteOffset) byteOffset;
@property (TB,N,V_dereference) dereference;
@property (TQ,N,V_bindIndex) bindIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLFunctionStitchingInputBufferAddress formattedDescription:];
-[MTLFunctionStitchingInputBufferAddress dereference];
-[MTLFunctionStitchingInputBufferAddress setByteOffset:];
-[MTLFunctionStitchingInputBufferAddress bindIndex];
-[MTLFunctionStitchingInputBufferAddress setDereference:];
-[MTLFunctionStitchingInputBufferAddress setBindIndex:];
-[MTLFunctionStitchingInputBufferAddress initWithBindIndex:byteOffset:dereference:];
-[MTLFunctionStitchingInputBufferAddress initWithBindIndex:];
-[MTLFunctionStitchingInputBufferAddress hash];
-[MTLFunctionStitchingInputBufferAddress byteOffset];
-[MTLFunctionStitchingInputBufferAddress description];
-[MTLFunctionStitchingInputBufferAddress copyWithZone:];
-[MTLFunctionStitchingInputBufferAddress isEqual:];
```
