# `MTLConstantRelocation`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLRelocation`
- 2 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSString" _symbolName;
@"NSObject<OS_dispatch_data>" _data;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_data>",R,N,V_data) data;
@property (T@"NSString",R,N,V_symbolName) symbolName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLConstantRelocation symbolName];
-[MTLConstantRelocation data];
-[MTLConstantRelocation dealloc];
-[MTLConstantRelocation initWithSymbolName:bytes:length:];
-[MTLConstantRelocation initWithSymbolName:data:];
```
