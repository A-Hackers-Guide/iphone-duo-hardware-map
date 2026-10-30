# `MTLBinaryEntry`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_data>" _data;
@"NSArray" _importedLibraries;
@"NSArray" _importedSymbols;
@"NSArray" _linkedBitcodes;
@"NSObject<OS_dispatch_data>" _bitcode;
@"NSObject<OS_dispatch_data>" _airScript;
@"NSObject<OS_dispatch_data>" _reflectionBlock;
i _reflectionFlags;
Q _binaryPosition;
Q _index;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_data>",R,V_data) data;
@property (T@"NSArray",R,V_importedSymbols) importedSymbols;
@property (T@"NSArray",R,V_importedLibraries) importedLibraries;
@property (Ti,R,V_reflectionFlags) reflectionFlags;
@property (TQ,R,V_binaryPosition) binaryPosition;
@property (TQ,V_index) index;
@property (T@"NSObject<OS_dispatch_data>",&) bitcode;
@property (T@"NSObject<OS_dispatch_data>",&) airScript;
@property (T@"NSArray",&,V_linkedBitcodes) linkedBitcodes;
@property (T@"NSObject<OS_dispatch_data>",R,V_reflectionBlock) reflectionBlock;
```

## Instance methods

```
-[MTLBinaryEntry airScript];
-[MTLBinaryEntry linkedBitcodes];
-[MTLBinaryEntry importedLibraries];
-[MTLBinaryEntry internalInitWithData:reflectionBlock:binaryPosition:];
-[MTLBinaryEntry data];
-[MTLBinaryEntry dealloc];
-[MTLBinaryEntry initWithData:reflectionBlock:binaryPosition:];
-[MTLBinaryEntry initWithData:binaryPosition:];
-[MTLBinaryEntry index];
-[MTLBinaryEntry binaryPosition];
-[MTLBinaryEntry setIndex:];
-[MTLBinaryEntry setAirScript:];
-[MTLBinaryEntry bitcode];
-[MTLBinaryEntry description];
-[MTLBinaryEntry initWithData:importedSymbols:importedLibraries:];
-[MTLBinaryEntry addReflectionWithData:flag:];
-[MTLBinaryEntry reflectionBlock];
-[MTLBinaryEntry importedSymbols];
-[MTLBinaryEntry initWithData:];
-[MTLBinaryEntry reflectionFlags];
-[MTLBinaryEntry setBitcode:];
-[MTLBinaryEntry setLinkedBitcodes:];
-[MTLBinaryEntry initWithData:reflectionBlock:];
```
