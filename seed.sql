\c rbproduct 

INSERT INTO category (name, slug)
VALUES ('Rug','rugs')
VALUES ('Wrist rug','wrist-rugs')
VALUES ('Mug rug','mug-rugs')
VALUES ('Mirror rug','mirror-rugs')
VALUES ('Stickers & more','stickers')

INSERT INTO product (
    name, 
    price, 
    category_id, 
    description, 
    dimensions, 
    quantity,
    created_at,
    updated_at
) VALUES 
-- PRODUCTS 1-10
(
  'Tufted Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug with ghostly vibes.',
  '~ 24in x 24in',
  1,
  NOW(),
  NOW(),
),
(
  'Tufted Scooby-Doo dog tag',
  107,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Scooby-Doo. Recreation of the Cartoon Network classic Scooby-doo dog tag. ',
  '~ 24in x 24in',
  1,
  NOW(),
  NOW(),
),
(
  'Pokeball mug rugs | Set of 4',
  50,
  (SELECT id FROM category WHERE slug='mug-rugs'),
  'From the franchise of Pokemon. Pokemon inspired rug coasters for your coffee, tea, juices or any other drinks.
  Set of 4. Classic Pokeball, Greatball, Ultraball, and Masterball',
  '6in x 6in',
  1,
  NOW(),
  NOW(),
),
(
  'Werk Rupaul Drag Race',
  75,
  (SELECT id FROM category WHERE slug='wrist-rugs'),
  'Rupaul Drag Race Werk. ',
  '14in x 10in',
  1,
  NOW(),
  NOW(),
),
(
  'Powerpuff Girl Heart Mirror',
  30,
  (SELECT id FROM category WHERE slug='mirror-rugs'),
  'From the franchise of Powerpuff girls. Inspired by the cartoon network Powerpuff Girls intro.',
  '4in x 4in',
  3,
  NOW(),
  NOW(),
),
(
  'Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug. Nonslip-backing',
  '2x2',
  1,
  NOW(),
  NOW(),
),
(
  'Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug. Nonslip-backing',
  '2x2',
  1,
  NOW(),
  NOW(),
),
(
  'Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug. Nonslip-backing',
  '2x2',
  1,
  NOW(),
  NOW(),
),
(
  'Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug. Nonslip-backing',
  '2x2',
  1,
  NOW(),
  NOW(),
),
(
  'Pixel Gengar Sprite',
  257,
  (SELECT id FROM category WHERE slug='rugs'),
  'From the franchise of Pokemon. A pixel art Gengar sprite rug. Nonslip-backing',
  '2x2',
  1,
  NOW(),
  NOW(),
),
