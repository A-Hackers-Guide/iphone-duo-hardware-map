# `MTKMesh`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSMutableArray" _submeshes;
@"NSMutableArray" _vertexBuffers;
@"MDLVertexDescriptor" _vertexDescriptor;
Q _vertexCount;
@"NSString" _name;
```

## Properties

```
@property (T@"NSArray",R,N,V_vertexBuffers) vertexBuffers;
@property (T@"MDLVertexDescriptor",R,N,V_vertexDescriptor) vertexDescriptor;
@property (T@"NSArray",R,N,V_submeshes) submeshes;
@property (TQ,R,N,V_vertexCount) vertexCount;
@property (T@"NSString",C,N,V_name) name;
```

## Class methods

```
+[MTKMesh _createMeshesFromObject:newMeshes:sourceMeshes:device:error:];
+[MTKMesh newMeshesFromAsset:device:sourceMeshes:error:];
```

## Instance methods

```
-[MTKMesh vertexBuffers];
-[MTKMesh vertexDescriptor];
-[MTKMesh vertexCount];
-[MTKMesh setName:];
-[MTKMesh name];
-[MTKMesh submeshes];
-[MTKMesh initWithMesh:device:error:];
```
