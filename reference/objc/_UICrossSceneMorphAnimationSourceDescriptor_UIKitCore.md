# `_UICrossSceneMorphAnimationSourceDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSXPCSecureCoding`, `BSDescriptionStreaming`, `_UICrossSceneMorphAnimationSourceGeometryProvider`, `_UICrossSceneMorphAnimationSourceViewProvider`
- 6 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
I contextId;
Q renderId;
{CGRect={CGPoint=dd}{CGSize=dd}} frameInSceneScreen;
@"_UICrossSceneMorphAnimationSourceDescriptorBackgroundDescriptor" backgroundDescriptor;
morphView;
scene;
```

## Properties

```
@property (TI,N,R,VcontextId) contextId;
@property (TQ,N,R,VrenderId) renderId;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R,VframeInSceneScreen) frameInSceneScreen;
@property (T@"_UICrossSceneMorphAnimationSourceDescriptorBackgroundDescriptor",N,&,VbackgroundDescriptor) backgroundDescriptor;
@property (Tq,N,R) hash;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Class methods

```
+[_UICrossSceneMorphAnimationSourceDescriptor supportsBSXPCSecureCoding];
```

## Instance methods

```
-[_UICrossSceneMorphAnimationSourceDescriptor contextId];
-[_UICrossSceneMorphAnimationSourceDescriptor debugDescription];
-[_UICrossSceneMorphAnimationSourceDescriptor init];
-[_UICrossSceneMorphAnimationSourceDescriptor hash];
-[_UICrossSceneMorphAnimationSourceDescriptor description];
-[_UICrossSceneMorphAnimationSourceDescriptor appendDescriptionToStream:];
-[_UICrossSceneMorphAnimationSourceDescriptor encodeWithBSXPCCoder:];
-[_UICrossSceneMorphAnimationSourceDescriptor initWithBSXPCCoder:];
-[_UICrossSceneMorphAnimationSourceDescriptor copyWithZone:];
-[_UICrossSceneMorphAnimationSourceDescriptor isEqual:];
-[_UICrossSceneMorphAnimationSourceDescriptor backgroundDescriptor];
-[_UICrossSceneMorphAnimationSourceDescriptor frameInSceneScreen];
-[_UICrossSceneMorphAnimationSourceDescriptor frameInUIView:completion:];
-[_UICrossSceneMorphAnimationSourceDescriptor initWithContextId:renderId:frameInSceneScreen:];
-[_UICrossSceneMorphAnimationSourceDescriptor initWithSourceUIBarButtonItem:];
-[_UICrossSceneMorphAnimationSourceDescriptor initWithSourceUIView:];
-[_UICrossSceneMorphAnimationSourceDescriptor makeSourceReplicaUIView];
-[_UICrossSceneMorphAnimationSourceDescriptor renderId];
-[_UICrossSceneMorphAnimationSourceDescriptor setBackgroundDescriptor:];
```
