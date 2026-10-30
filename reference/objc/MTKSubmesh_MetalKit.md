# `MTKSubmesh`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _primitiveType;
Q _indexType;
@"MTKMeshBuffer" _indexBuffer;
Q _indexCount;
@"MTKMesh" _mesh;
@"NSString" _name;
```

## Properties

```
@property (TQ,R,N,V_primitiveType) primitiveType;
@property (TQ,R,N,V_indexType) indexType;
@property (T@"MTKMeshBuffer",R,N,V_indexBuffer) indexBuffer;
@property (TQ,R,N,V_indexCount) indexCount;
@property (T@"MTKMesh",R,W,N,V_mesh) mesh;
@property (T@"NSString",C,N,V_name) name;
```

## Instance methods

```
-[MTKSubmesh indexType];
-[MTKSubmesh setName:];
-[MTKSubmesh primitiveType];
-[MTKSubmesh name];
-[MTKSubmesh mesh];
-[MTKSubmesh indexCount];
-[MTKSubmesh indexBuffer];
-[MTKSubmesh initWithMesh:submesh:device:error:];
```
