# `MTLRenderPipelineFunctionsDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _vertexAdditionalBinaryFunctions;
@"NSArray" _fragmentAdditionalBinaryFunctions;
@"NSArray" _tileAdditionalBinaryFunctions;
@"NSArray" _objectAdditionalBinaryFunctions;
@"NSArray" _meshAdditionalBinaryFunctions;
^Q _vertexAdditionalBinaryFunctionResourceIndices;
^Q _fragmentAdditionalBinaryFunctionResourceIndices;
^Q _tileAdditionalBinaryFunctionResourceIndices;
^Q _objectAdditionalBinaryFunctionResourceIndices;
^Q _meshAdditionalBinaryFunctionResourceIndices;
```

## Properties

```
@property (T@"NSArray",C,N,V_objectAdditionalBinaryFunctions) objectAdditionalBinaryFunctions;
@property (T@"NSArray",C,N,V_meshAdditionalBinaryFunctions) meshAdditionalBinaryFunctions;
@property (T^Q,N,V_vertexAdditionalBinaryFunctionResourceIndices) vertexAdditionalBinaryFunctionResourceIndices;
@property (T^Q,N,V_fragmentAdditionalBinaryFunctionResourceIndices) fragmentAdditionalBinaryFunctionResourceIndices;
@property (T^Q,N,V_tileAdditionalBinaryFunctionResourceIndices) tileAdditionalBinaryFunctionResourceIndices;
@property (T^Q,N,V_objectAdditionalBinaryFunctionResourceIndices) objectAdditionalBinaryFunctionResourceIndices;
@property (T^Q,N,V_meshAdditionalBinaryFunctionResourceIndices) meshAdditionalBinaryFunctionResourceIndices;
@property (T@"NSArray",C,N,V_vertexAdditionalBinaryFunctions) vertexAdditionalBinaryFunctions;
@property (T@"NSArray",C,N,V_fragmentAdditionalBinaryFunctions) fragmentAdditionalBinaryFunctions;
@property (T@"NSArray",C,N,V_tileAdditionalBinaryFunctions) tileAdditionalBinaryFunctions;
```

## Instance methods

```
-[MTLRenderPipelineFunctionsDescriptor init];
-[MTLRenderPipelineFunctionsDescriptor dealloc];
-[MTLRenderPipelineFunctionsDescriptor hash];
-[MTLRenderPipelineFunctionsDescriptor copyWithZone:];
-[MTLRenderPipelineFunctionsDescriptor isEqual:];
-[MTLRenderPipelineFunctionsDescriptor vertexAdditionalBinaryFunctions];
-[MTLRenderPipelineFunctionsDescriptor objectAdditionalBinaryFunctions];
-[MTLRenderPipelineFunctionsDescriptor fragmentAdditionalBinaryFunctionResourceIndices];
-[MTLRenderPipelineFunctionsDescriptor fragmentAdditionalBinaryFunctions];
-[MTLRenderPipelineFunctionsDescriptor meshAdditionalBinaryFunctionResourceIndices];
-[MTLRenderPipelineFunctionsDescriptor meshAdditionalBinaryFunctions];
-[MTLRenderPipelineFunctionsDescriptor objectAdditionalBinaryFunctionResourceIndices];
-[MTLRenderPipelineFunctionsDescriptor setFragmentAdditionalBinaryFunctionResourceIndices:];
-[MTLRenderPipelineFunctionsDescriptor setFragmentAdditionalBinaryFunctions:];
-[MTLRenderPipelineFunctionsDescriptor setMeshAdditionalBinaryFunctionResourceIndices:];
-[MTLRenderPipelineFunctionsDescriptor setMeshAdditionalBinaryFunctions:];
-[MTLRenderPipelineFunctionsDescriptor setObjectAdditionalBinaryFunctionResourceIndices:];
-[MTLRenderPipelineFunctionsDescriptor setObjectAdditionalBinaryFunctions:];
-[MTLRenderPipelineFunctionsDescriptor setTileAdditionalBinaryFunctionResourceIndices:];
-[MTLRenderPipelineFunctionsDescriptor setTileAdditionalBinaryFunctions:];
-[MTLRenderPipelineFunctionsDescriptor setVertexAdditionalBinaryFunctionResourceIndices:];
-[MTLRenderPipelineFunctionsDescriptor setVertexAdditionalBinaryFunctions:];
-[MTLRenderPipelineFunctionsDescriptor tileAdditionalBinaryFunctionResourceIndices];
-[MTLRenderPipelineFunctionsDescriptor tileAdditionalBinaryFunctions];
-[MTLRenderPipelineFunctionsDescriptor vertexAdditionalBinaryFunctionResourceIndices];
```
