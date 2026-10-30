# `TUConversationActivitySceneAssociationBehavior`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _shouldAssociateScene;
@"NSString" _targetContentIdentifier;
@"NSString" _preferredSceneSessionRole;
```

## Properties

```
@property (T@"NSString",R,C,N,V_targetContentIdentifier) targetContentIdentifier;
@property (TB,R,N,V_shouldAssociateScene) shouldAssociateScene;
@property (T@"NSString",R,C,N,V_preferredSceneSessionRole) preferredSceneSessionRole;
```

## Class methods

```
+[TUConversationActivitySceneAssociationBehavior supportsSecureCoding];
+[TUConversationActivitySceneAssociationBehavior defaultBehavior];
```

## Instance methods

```
-[TUConversationActivitySceneAssociationBehavior targetContentIdentifier];
-[TUConversationActivitySceneAssociationBehavior encodeWithCoder:];
-[TUConversationActivitySceneAssociationBehavior hash];
-[TUConversationActivitySceneAssociationBehavior description];
-[TUConversationActivitySceneAssociationBehavior initWithCoder:];
-[TUConversationActivitySceneAssociationBehavior copyWithZone:];
-[TUConversationActivitySceneAssociationBehavior isEqual:];
-[TUConversationActivitySceneAssociationBehavior initWithTargetContentIdentifier:shouldAssociateScene:preferredSceneSessionRole:];
-[TUConversationActivitySceneAssociationBehavior isEquivalentToSceneAssociationBehavior:];
-[TUConversationActivitySceneAssociationBehavior preferredSceneSessionRole];
-[TUConversationActivitySceneAssociationBehavior shouldAssociateScene];
```
