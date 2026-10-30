# `MTLBufferRelocation`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLRelocation`
- 3 instance variables, 7 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _symbolName;
@"<MTLBuffer>" _buffer;
Q _offset;
```

## Properties

```
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R,N,V_offset) offset;
@property (T@"NSString",R,N,V_symbolName) symbolName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLBufferRelocation buffer];
-[MTLBufferRelocation symbolName];
-[MTLBufferRelocation dealloc];
-[MTLBufferRelocation offset];
-[MTLBufferRelocation initWithSymbolName:buffer:offset:];
```
