# Index des Formes Conceptuelles Dynamiques — Axes et Formalisation V2.1.2

## Espace d'états

Un système est un point dans le cube unité à 5 dimensions :

```
x = (A1, A2, A3, A4, A5) ∈ [0,1]⁵
```

## Hypothèse structurelle V2

L'espace morphologique réel n'est pas (A1, A2, A3, A4, A5).

Il est principalement :

```
(Δ₂₃, Δ₄₅, Δ₁₂)
```

Les axes absolus servent de qualificateurs d'intensité (niveau 2), pas de discriminants primaires.

Cette hypothèse est issue de la batterie de 15 cas hétérogènes : les formes se reconnaissent par les *relations entre axes* (gradients), pas par les niveaux absolus de chaque axe.

---

## Les 5 axes

### A1 — Complexité organisationnelle

**Définition :** Nombre et profondeur des niveaux de transformation nécessaires pour produire l'état global du système.

**Ce que ce n'est pas :** la taille, le nombre brut d'éléments, l'interdépendance, l'intensité.

**Proxies formels :** profondeur de graphe, niveaux hiérarchiques, longueur moyenne des chaînes causales, profondeur de pipeline.

### A2 — Couplage structurel interne

**Définition :** Sensibilité globale du système à une modification locale. Si Δe local → ΔS global significatif, le couplage est élevé.

**Ce que ce n'est pas :** la profondeur, la complexité, la normativité, la stabilité.

**Proxies formels :** connectivité moyenne, propagation de perturbation, dépendance systémique, dérivée globale / perturbations locales.

### A3 — Intégration informationnelle

**Définition :** Degré de réduction de variance globale produit par la coordination interne des sous-processus.

**Distinction avec A2 :** Couplage = propagation des perturbations. Intégration = réduction d'incertitude par coordination. Un système peut être fortement couplé mais peu intégré (propagation chaotique sans stabilisation).

**Proxies formels :** compatible avec théorie de l'information, entropie conditionnelle, mutual information.

### A4 — Normativité régulatoire

**Définition :** Capacité d'un système à restreindre son espace d'états en produisant et maintenant une région préférentielle R ⊂ Ω par mécanismes internes de correction.

**Ce que cela exclut :** intention, valeur morale, conscience, téléologie métaphysique.

**Distinction cruciale :** normativité interne (produite par le système) vs imposée (extrinsèque). Un LLM avec RLHF a une normativité imposée, pas produite.

### A5 — Capacité de révision interne

**Définition :** Capacité d'un système à modifier ses propres mécanismes régulatoires (D) ou les critères définissant sa région d'états admissibles (R).

**Distinction avec A4 :** A4 = appliquer R (réguler). A5 = modifier R ou D (méta-réguler).

---

## Les 5 gradients structurels

Les gradients sont les opérateurs diagnostiques primaires de l'index. Chacun capte une *relation* entre deux axes.

| Gradient | Formule | Ce qu'il capte |
|---|---|---|
| Δ₂₃ | A2 − A3 | Couplage vs intégration. Positif = propagation > stabilisation. |
| Δ₄₅ | A4 − A5 | Normativité vs révision. Positif = régulation > méta-régulation. |
| Δ₁₂ | A1 − A2 | Profondeur vs propagation. Positif = structure > couplage = inertie. |
| Δ₃₅ | A3 − A5 | Intégration vs révision. Élevé = cohérence maintenue sans révision. |
| Δ₄₃ | A4 − A3 | Normativité vs intégration. Positif = norme > cohérence réelle. |

### Pourquoi les gradients sont primaires

Deux systèmes peuvent avoir le même Δ₄₅ = 0.45 avec des profils très différents : A4=0.50/A5=0.05 (thermostat, rigidification douce) vs A4=0.75/A5=0.30 (organisme multicellulaire, rigidification lourde). Le gradient identifie le *type* de régime. Les axes absolus qualifient son *intensité*.

---

## Classification V2.1.2 : deux niveaux

### Niveau 1 — Typage par gradients

Les formes sont définies par des conditions sur les gradients (poids 2.0-2.5).

| Forme | Gradient primaire | Condition |
|---|---|---|
| F01 Équilibre différentiel | Δ₂₃, Δ₄₅ | Δ₂₃ ≤ 0.18 ET Δ₄₅ ≤ 0.30 |
| F03 Sur-couplage | Δ₂₃ | Δ₂₃ ≥ 0.23 |
| F04 Plateau inertiel | Δ₃₅, Δ₁₂ | Δ₃₅ ≥ 0.35 ET Δ₁₂ ≥ 0.15 |
| F05 Dominance normative | Δ₄₅ | Δ₄₅ ≥ 0.40 |
| F06 Inversion normative | Δ₄₅ | Δ₄₅ ≤ 0.05 (A5 ≥ A4) |
| F08 Dissolution fonctionnelle | Δ₄₃, Δ₁₂ | Δ₄₃ ≥ 0.25 ET Δ₁₂ ≥ 0.20 |
| F09 Architecture pure | Δ₄₃ | Δ₄₃ ≤ -0.40 (intégration >> normativité) |

### Niveau 2 — Intensité par axes absolus

Les axes absolus qualifient la densité du régime (poids 0.8-1.5). Par exemple, F05 exige A4 ≥ 0.45 (normativité substantielle) et A5 ≤ 0.30 (révision faible), mais ces conditions sont secondaires par rapport au gradient Δ₄₅.

### Distance et classification

```
d_F(x) = Σ w_j · max(0, g_j(x))

F̂(x) = argmin_F d_F(x)
```

Le classifieur est explicable : chaque contrainte est identifiée comme gradient ou absolue, avec sa violation et sa marge.

---

## Les 7 formes

### F01 — Équilibre différentiel

**Signature :** Δ₂₃ ≤ 0.18, Δ₄₅ ≤ 0.30

La propagation et l'intégration sont synchrones. La normativité et la révision sont en équilibre. Le système absorbe les perturbations sans que la propagation dépasse la stabilisation, et régule sans verrouiller sa capacité de révision.

**Qualificateurs :** A3 ≥ 0.40, A4 ≥ 0.25, A5 ≥ 0.15, A4 ≤ 0.70.

**Cas validés :** Cellule eucaryote, Immunité adaptative, Ve République, Apple, TikTok, Linux, Physique théorique.

### F03 — Sur-couplage

**Signature :** Δ₂₃ ≥ 0.23

La propagation dépasse significativement l'intégration. Les perturbations se diffusent plus vite que le système ne les stabilise. La normativité est typiquement débordée.

**Qualificateurs :** A4 ≤ 0.50, A2 ≥ 0.55.

**Cas validés :** Marché NYSE, Supply chain.

### F04 — Plateau inertiel

**Signature :** Δ₃₅ ≥ 0.35, Δ₁₂ ≥ 0.15

L'intégration est élevée par rapport à la révision (cohérence sans évolution), et la profondeur dépasse la propagation (structure sans couplage = inertie). Le système est « plein » — optimisé mais non révisable.

**Qualificateurs :** A1 ≥ 0.60, A5 ≤ 0.30.

**Cas validés :** Église, Organisme multicellulaire, LLM statique, Ordre réformé.

### F05 — Dominance normative

**Signature :** Δ₄₅ ≥ 0.40

La normativité domine fortement la révision. Le système régule agressivement sans jamais réviser ses critères. La sévérité dépend de l'intensité absolue de A4 : un thermostat (A4=0.50) est une dominance douce, un régime autoritaire (A4=0.80) est une dominance lourde.

**Qualificateurs :** A4 ≥ 0.45, A5 ≤ 0.30.

**Cas validés :** Thermostat, Église, Organisme multicellulaire, Régime autoritaire, Ordre réformé.

### F06 — Inversion normative

**Signature :** Δ₄₅ ≤ 0.05, A5 ≥ 0.50

La révision égale ou dépasse la normativité. Le système est en phase de réorganisation active — il modifie ses propres règles plutôt que de simplement les appliquer. La propagation est stabilisée (Δ₂₃ ≤ 0.18).

**Qualificateurs :** A3 ≥ 0.45.

**Cas validés :** Linux, Physique théorique. Immunité adaptative proche (runner-up à d=0.125).

### F08 — Dissolution fonctionnelle

**Signature :** Δ₄₃ ≥ 0.25, Δ₁₂ ≥ 0.20

La normativité dépasse significativement l'intégration (les normes persistent mais ne stabilisent plus rien), et la structure dépasse le couplage (l'architecture existe mais ne propage plus). Le système « existe sans fonctionner ».

**Qualificateurs :** A3 ≤ 0.40, A5 ≤ 0.20.

**Cas validés :** Aucun cas net dans la batterie actuelle. Régime autoritaire est runner-up proche (d=0.375).

### F09 — Architecture pure

**Signature :** Δ₄₃ ≤ -0.40, A4 ≤ 0.15, A5 ≤ 0.10

L'intégration est très supérieure à la normativité. Le système n'a aucun mécanisme interne de correction ni de révision — il ne « se régule pas ». C'est une structure qui fonctionne sans se maintenir. Forme ajoutée en V2 pour capturer les systèmes que V1 ne classifiait pas bien.

**Qualificateurs :** A3 ≥ 0.50, A1 ≥ 0.60.

**Cas validés :** LLM statique (à égalité avec F04).

---

## Chevauchements et zones de transition

V2 admet explicitement que des systèmes puissent être dans plusieurs formes simultanément. Ce ne sont pas des défauts — ce sont des zones de transition structurelles.

| Système | Formes simultanées | Interprétation |
|---|---|---|
| Église | F04 ∩ F05 | Plateau inertiel + dominance normative : rigidification sur un plateau saturé |
| Organisme multicellulaire | F04 ∩ F05 | Même configuration : structure achevée + normativité dominante |
| Ordre réformé | F04 ∩ F05 | Même configuration |
| LLM statique | F04 ∩ F09 | Plateau inertiel + architecture sans normativité |
| Linux | F01 ∩ F06 | Équilibre + inversion normative : homéostasie avec capacité de révision élevée |
| Physique théorique | F01 ∩ F06 | Même configuration : discipline vivante qui se révise activement |

Les chevauchements F04 ∩ F05 (plateau + dominance) et F01 ∩ F06 (équilibre + inversion) sont les deux zones de transition les plus peuplées. Ils correspondent à deux « corridors » dans l'espace des gradients :

- **Corridor rigide :** Δ₃₅ élevé + Δ₄₅ élevé. Systèmes intégrés, normatifs, non révisables.
- **Corridor vivant :** Δ₂₃ ≈ 0 + Δ₄₅ ≈ 0. Systèmes équilibrés avec capacité de révision active.

---

## Surfaces de transition

### F01 → F03 (vers le sur-couplage)
```
Δ₂₃ franchit 0.18 vers le haut
Mécanisme : la propagation augmente ou l'intégration diminue
```

### F01 → F05 (vers la dominance normative)
```
Δ₄₅ franchit 0.30 vers le haut
Mécanisme : la normativité augmente sans que la révision suive
```

### F03 → F06 (vers l'inversion normative)
```
Δ₄₅ passe sous 0.05, A5 franchit 0.50
Mécanisme : la crise force une révision des règles
```

### F06 → F01 (vers l'équilibre)
```
Δ₄₅ remonte vers 0.20, A5 redescend
Mécanisme : le nouveau régime se stabilise
```

### F04 → F05 (du plateau vers la dominance)
```
Δ₄₅ franchit 0.40
Mécanisme : la saturation est traitée par sur-normativité
```

### F05 → F03 (la rigidité casse)
```
Δ₂₃ franchit 0.23
Mécanisme : une perturbation brise les mécanismes figés
```

### Cycle minimal vérifié : F01 → F03 → F06 → F01
```
Δ₂₃ ↑ → Δ₄₅ ↓ → Δ₄₅ ↑
```

---

## Validation empirique

### Batterie de 15 cas (V2.1.2)

| # | Système | A1 | A2 | A3 | A4 | A5 | Best | 2nd | Inside |
|---|---|---|---|---|---|---|---|---|---|
| 01 | Cellule eucaryote | 0.70 | 0.60 | 0.75 | 0.65 | 0.35 | F01 | F04 | ★ |
| 02 | Thermostat | 0.20 | 0.40 | 0.45 | 0.50 | 0.00 | F05 | F01 | ★ |
| 03 | Marché NYSE | 0.60 | 0.75 | 0.50 | 0.30 | 0.20 | F03 | F01 | ★ |
| 04 | Immunité adaptative | 0.75 | 0.65 | 0.70 | 0.65 | 0.55 | F01 | F06 | ★ |
| 05 | Église | 0.80 | 0.55 | 0.60 | 0.75 | 0.10 | F04 | F05 | ★ |
| 06 | Ve République | 0.65 | 0.60 | 0.55 | 0.60 | 0.40 | F01 | F06 | ★ |
| 07 | Organisme multicellulaire | 0.85 | 0.70 | 0.80 | 0.75 | 0.30 | F04 | F05 | ★ |
| 08 | Régime autoritaire | 0.70 | 0.65 | 0.45 | 0.80 | 0.05 | F05 | F04 | ★ |
| 09 | Supply chain | 0.55 | 0.80 | 0.45 | 0.35 | 0.15 | F03 | F01 | ★ |
| 10 | Apple | 0.75 | 0.65 | 0.70 | 0.70 | 0.50 | F01 | F06 | ★ |
| 11 | TikTok | 0.60 | 0.75 | 0.65 | 0.55 | 0.45 | F01 | F06 | ★ |
| 12 | LLM statique | 0.90 | 0.55 | 0.75 | 0.05 | 0.00 | F04 | F09 | ★ |
| 13 | Linux | 0.70 | 0.55 | 0.70 | 0.60 | 0.55 | F01 | F06 | ★ |
| 14 | Ordre réformé | 0.75 | 0.50 | 0.65 | 0.70 | 0.25 | F04 | F05 | ★ |
| 15 | Physique théorique | 0.70 | 0.55 | 0.65 | 0.55 | 0.60 | F01 | F06 | ★ |

**Résultat : 15/15 inside** (contre 3/15 en V1).

### Gains V1 → V2 → V2.1.2

| Métrique | V1 | V2 | V2.1.2 |
|---|---|---|---|
| Cas inside | 3/15 | 15/15 | 15/15 |
| Formes | 6 | 7 (+ F09) | 7 |
| Logique primaire | Seuils absolus | Gradients structurels | Gradients + frontière F01/F03 resserrée |
| Chevauchements | Non gérés | Explicites | Explicites |
| Zone grise F01↔F03 | — | [0.15, 0.25] (écart 0.10) | [0.18, 0.23] (écart 0.05) |

---

## Protocole d'usage

1. Ne pas convertir cohérence en existence
2. Ne pas déduire couplage de complexité (A1 ⊥ A2)
3. Ne pas confondre normativité et valeur morale
4. Distinguer normativité interne et imposée
5. Tester les désynchronisations (les gradients sont plus informatifs que les axes)
6. Accepter les résultats contre-intuitifs
7. Accepter les chevauchements (F04 ∩ F05, F01 ∩ F06) — ce sont des zones de transition
8. Ne pas ajouter d'axe sans test d'indépendance sur 5+ systèmes hétérogènes

---

## Grille d'interprétation

### Axes absolus (intensité)

| Score | Interprétation |
|---|---|
| 0.0 – 0.2 | Absent ou négligeable |
| 0.2 – 0.4 | Présent mais faible |
| 0.4 – 0.6 | Modéré |
| 0.6 – 0.8 | Élevé |
| 0.8 – 1.0 | Très élevé |

### Gradients (typage)

| Gradient | Valeur | Interprétation |
|---|---|---|
| Δ₂₃ < -0.10 | Intégration domine le couplage — stabilisation efficace |
| Δ₂₃ ∈ [-0.10, 0.18] | Zone d'équilibre (F01) |
| Δ₂₃ ∈ [0.18, 0.23] | Zone grise — pression vers F03 |
| Δ₂₃ > 0.23 | Sur-couplage (F03) |
| Δ₄₅ < 0.05 | Inversion normative (F06) — révision ≥ normativité |
| Δ₄₅ ∈ [0.05, 0.30] | Zone d'équilibre (F01) |
| Δ₄₅ ∈ [0.30, 0.40] | Zone grise — pression vers F05 |
| Δ₄₅ > 0.40 | Dominance normative (F05) |

---

## Candidates pour axes futurs

| Candidat | Raison | Statut |
|---|---|---|
| Ouverture au milieu | Couplage externe (≠ A2 interne) | À formaliser |
| Transmissibilité | Portabilité inter-substrats | À formaliser |
| Symbolisation | Opération par représentations détachées | À formaliser |
