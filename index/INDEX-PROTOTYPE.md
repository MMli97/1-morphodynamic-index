# Index des Formes Conceptuelles Dynamiques — Prototype V2.1.2

## Architecture du classifieur

### Deux niveaux

**Niveau 1 — Typage par gradients.** Les formes sont identifiées par les relations entre axes (Δ₂₃, Δ₄₅, Δ₁₂, Δ₃₅, Δ₄₃). Les gradients portent un poids de 2.0 à 2.5 dans le calcul de distance.

**Niveau 2 — Intensité par axes absolus.** Les valeurs absolues (A1 à A5) qualifient la densité du régime. Poids de 0.8 à 1.5.

### Pourquoi cette architecture

La batterie de 15 cas a montré que les seuils absolus de V1 excluaient artificiellement des systèmes bien typés. Le thermostat (A4=0.50) était clairement une rigidification mais sortait du polytope (A4 ≥ 0.65). L'immunité adaptative (A1=0.75) était clairement homéostatique mais sortait du polytope (A1 ≤ 0.65). Le passage aux gradients comme opérateurs primaires résout ces problèmes : le *type* de régime dépend de la relation entre axes, pas de leur niveau absolu.

---

## Les 7 formes

### F01 — Équilibre différentiel
**Gradient :** Δ₂₃ ≤ 0.18, Δ₄₅ ≤ 0.30
Le système absorbe ce qu'il propage, et régule sans verrouiller sa révision. C'est la forme la plus « peuplée » de la batterie (7 cas), ce qui est attendu — l'équilibre est le régime par défaut des systèmes fonctionnels.

### F03 — Sur-couplage
**Gradient :** Δ₂₃ ≥ 0.23
La propagation dépasse l'intégration. Les perturbations se diffusent sans être stabilisées. Forme la plus rare dans la batterie (2 cas : NYSE, Supply chain), ce qui est aussi attendu — la crise est transitoire par nature.

### F04 — Plateau inertiel
**Gradient :** Δ₃₅ ≥ 0.35, Δ₁₂ ≥ 0.15
Intégration sans révision, profondeur sans propagation. Le système est structurellement achevé mais non évolutif. Souvent en chevauchement avec F05.

### F05 — Dominance normative
**Gradient :** Δ₄₅ ≥ 0.40
La normativité écrase la révision. Le système régule agressivement sans modifier ses critères. L'intensité varie fortement : thermostat (dominance douce, A4=0.50) vs régime autoritaire (dominance lourde, A4=0.80).

### F06 — Inversion normative
**Gradient :** Δ₄₅ ≤ 0.05, A5 ≥ 0.50
La révision égale ou dépasse la normativité. Le système se réorganise activement. Souvent en chevauchement avec F01 (les systèmes « vivants » qui se révisent sont aussi en équilibre). Propagation stabilisée (Δ₂₃ ≤ 0.18).

### F08 — Dissolution fonctionnelle
**Gradient :** Δ₄₃ ≥ 0.25, Δ₁₂ ≥ 0.20
La norme persiste sans intégrer, la structure existe sans coupler. Aucun cas net dans la batterie actuelle — la dissolution est un régime extrême.

### F09 — Architecture pure
**Gradient :** Δ₄₃ ≤ -0.40, A4 ≤ 0.15
L'intégration est très supérieure à la normativité. Le système n'a aucun mécanisme de correction interne. Forme ajoutée en V2 pour capturer les systèmes sans régulation (LLM en inférence).

---

## Résultats sur la batterie de 15 cas

### Classifications

| # | Système | Δ₂₃ | Δ₄₅ | Δ₁₂ | Best | 2nd | Chevauchement |
|---|---|---|---|---|---|---|---|
| 01 | Cellule eucaryote | -0.15 | +0.30 | +0.10 | F01 | F04 | — |
| 02 | Thermostat | -0.05 | +0.50 | -0.20 | F05 | F01 | — |
| 03 | Marché NYSE | +0.25 | +0.10 | -0.15 | F03 | F01 | — |
| 04 | Immunité adaptative | -0.05 | +0.10 | +0.10 | F01 | F06 | — |
| 05 | Église | -0.05 | +0.65 | +0.25 | F04 | F05 | F04 ∩ F05 |
| 06 | Ve République | +0.05 | +0.20 | +0.05 | F01 | F06 | — |
| 07 | Organisme multicellulaire | -0.10 | +0.45 | +0.15 | F04 | F05 | F04 ∩ F05 |
| 08 | Régime autoritaire | +0.20 | +0.75 | +0.05 | F05 | F04 | — |
| 09 | Supply chain | +0.35 | +0.20 | -0.25 | F03 | F01 | — |
| 10 | Apple | -0.05 | +0.20 | +0.10 | F01 | F06 | — |
| 11 | TikTok | +0.10 | +0.10 | -0.15 | F01 | F06 | — |
| 12 | LLM statique | -0.20 | +0.05 | +0.35 | F04 | F09 | F04 ∩ F09 |
| 13 | Linux | -0.15 | +0.05 | +0.15 | F01 | F06 | F01 ∩ F06 |
| 14 | Ordre réformé | -0.15 | +0.45 | +0.25 | F04 | F05 | F04 ∩ F05 |
| 15 | Physique théorique | -0.10 | -0.05 | +0.15 | F01 | F06 | F01 ∩ F06 |

### Observations structurelles

**Δ₂₃ est le discriminant le plus puissant.** Il sépare nettement les systèmes en crise (NYSE +0.25, Supply chain +0.35) des systèmes en équilibre (cellule -0.15, Linux -0.15). La zone grise [0.18, 0.23] est étroite et bien calibrée.

**Δ₄₅ est le deuxième discriminant.** Il sépare les systèmes rigides (autoritaire +0.75, Église +0.65, thermostat +0.50) des systèmes vivants (Linux +0.05, physique -0.05, immunité +0.10). Le seuil 0.40 pour F05 est bien placé.

**Δ₁₂ est le moins discriminant des trois principaux.** Il contribue à la séparation F04/F08 mais ne porte pas de forme à lui seul. Il distingue les systèmes inertiels (LLM +0.35, Église +0.25) des systèmes « plats » (Supply chain -0.25, TikTok -0.15).

**Les chevauchements sont systématiques et informatifs.** Deux corridors apparaissent :
- **Corridor rigide (F04 ∩ F05)** : Église, Organisme, Ordre réformé. Systèmes à la fois saturés et normatifs — ils ont atteint leur forme finale et la maintiennent par normativité.
- **Corridor vivant (F01 ∩ F06)** : Linux, Physique théorique. Systèmes en équilibre qui conservent une capacité de révision active — ils fonctionnent *et* évoluent.

**Le LLM statique est le cas le plus singulier.** Il est dans F04 ∩ F09 — plateau inertiel + architecture pure. C'est le seul système de la batterie avec A4 ≈ 0 et A3 élevé. Il intègre sans réguler, ce qui est une configuration structurellement unique. Le Δ₄₃ = -0.70 est le plus extrême de toute la batterie.

---

## Cartographie des transitions

```
      F01 ──(Δ₂₃ ↑)──→ F03 ──(Δ₄₅ ↓)──→ F06
       ↑                  │                 │
       │                  │                 │
  (Δ₄₅ ↑)           (A3↓,A2↓)         (Δ₄₅ ↑)
       │                  │                 │
       │                  ▼                 ↓
      F05 ←──(Δ₄₅ ↑)── F04              F01
       │                  │
  (Δ₂₃ ↑)           (A3 ↓)
       │                  │
       ↓                  ▼
      F03               F08

Cycle minimal : F01 → F03 → F06 → F01
Via gradients : Δ₂₃ ↑ → Δ₄₅ ↓ → Δ₄₅ ↑
Seuils F01↔F03 : Δ₂₃ = 0.18 (sortie F01) / 0.23 (entrée F03)
```

---

## Pistes d'évolution

### Calibration

Les prochains cas de test devraient cibler les zones sous-peuplées :
- **F08 (Dissolution)** : aucun cas net. Tester sur un empire en effondrement, un département d'entreprise en cours de démantèlement, ou un organe nécrosé.
- **F06 (Inversion normative)** : seulement en chevauchement avec F01. Tester sur une start-up en pivot, un processus constituant, ou un réseau en refondation.
- **F09 (Architecture pure)** : seul le LLM. Tester sur une base de données, un réseau routier, ou un cristal.

### Axes manquants

La batterie confirme que les 5 axes captent la structure interne mais pas les relations inter-systèmes. F07 (Transmission) n'a pas été formalisée en V2 faute d'axe approprié. Trois candidats restent identifiés : ouverture au milieu, transmissibilité, symbolisation.

### Étalonnage inter-domaines

Le problème le plus important pour la publication : qu'est-ce que A2 = 0.65 veut dire pour une cellule vs pour un marché ? Les proxies formels (mutual information pour A3, connectivité pour A2) doivent être testés empiriquement sur quelques systèmes pour vérifier la convergence avec les scorings qualitatifs.
