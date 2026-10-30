# `/System/Library/PreferenceBundles/MobileSafariSettings.bundle/AutoFill.plist`

From the small APFS image 141-28395-106.dmg. 649 bytes.

- `items`:
  -
    - `cell`: `PSGroupCell`
    - `id`: `AutoFillSettingsHeaderGroupCell`
  -
    - `cell`: `PSGroupCell`
  -
    - `cell`: `PSSwitchCell`
    - `get`: `useContactInfo:`
    - `id`: `ContactInfoEnableSwitch`
    - `label`: `Use Contact Info`
    - `set`: `setUseContactInfo:forSpecifier:`
  -
    - `buttonAction`: `showMeCardPicker`
    - `cell`: `PSLinkListCell`
    - `get`: `myInfo:`
    - `label`: `My Info`
  -
    - `cell`: `PSGroupCell`
    - `id`: `CreditCardGroup`
  -
    - `cell`: `PSSwitchCell`
    - `get`: `shouldAutoFillCreditCards:`
    - `id`: `CreditCardEnableSwitch`
    - `label`: `Credit Cards`
    - `set`: `setShouldAutoFillCreditCards:specifier:`
  -
    - `cell`: `PSLinkListCell`
    - `detail`: `SafariSavedCreditCardsController`
    - `id`: `CreditCardList`
    - `label`: `Saved Credit Cards`
- `title`: `AutoFill`
