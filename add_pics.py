import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
import time
import requests
import os


user_bios = [
    "Passionate about self-improvement and learning from diverse communities.",
    "Seeking enlightenment through shared experiences and knowledge exchange.",
    "Embracing vulnerability as a pathway to personal growth.",
    "Believer in the power of community support for achieving goals.",
    "Dedicated to continuous self-discovery and development.",
    "Striving to cultivate a growth mindset in all aspects of life.",
    "On a journey of self-reflection and inner transformation.",
    "Committed to lifelong learning and self-improvement.",
    "Exploring different paths to fulfillment and self-actualization.",
    "Fostering connections with like-minded individuals for mutual growth.",
    "Advocate for holistic well-being and mindfulness practices.",
    "Finding strength in vulnerability and authenticity.",
    "Inspired by the collective wisdom of diverse communities.",
    "Passionate about fostering empathy and understanding.",
    "Championing self-love and acceptance as the foundation for growth.",
    "Embarking on a journey of personal evolution and self-discovery.",
    "Seeking inspiration from fellow travelers on the road to self-improvement.",
    "Embracing discomfort as a catalyst for growth and change.",
    "Advocate for mental health awareness and self-care practices.",
    "Driven by a desire to unlock my full potential.",
    "Striving for balance and harmony in mind, body, and spirit.",
    "On a quest for personal growth and self-realization.",
    "Empowering others through shared knowledge and experiences.",
    "Exploring the intersections of personal growth and social change.",
    "Believer in the transformative power of community engagement.",
    "Determined to overcome obstacles and thrive.",
    "Finding joy in the journey of self-discovery.",
    "Building resilience through adversity and challenges.",
    "Seeking clarity and purpose in every endeavor.",
    "Fueled by curiosity and a thirst for knowledge.",
    "Advocate for authenticity and living in alignment with values.",
    "Inspired by the potential for positive change within ourselves and our communities.",
    "Striving for excellence in every aspect of life.",
    "Embracing the journey of self-improvement with open arms.",
    "Committed to personal growth as a lifelong pursuit.",
    "On a mission to unlock the limitless potential within.",
    "Believer in the power of intention and conscious living.",
    "Finding strength in vulnerability and resilience in adversity.",
    "Championing self-awareness as the cornerstone of personal growth.",
    "Seeking wisdom from the collective intelligence of diverse communities.",
    "Embracing the beauty of imperfection on the path to self-mastery.",
    "Advocate for compassion and empathy in all interactions.",
    "Dedicated to cultivating a growth mindset in myself and others.",
    "Striving to be the best version of myself every day.",
    "On a journey of self-exploration and self-expression.",
    "Committed to creating positive change in myself and the world.",
    "Seeking inspiration from the journeys of fellow travelers.",
    "Embracing the challenges of growth with courage and resilience.",
    "Believer in the transformative power of self-reflection and introspection.",
    "Passionate about fostering a culture of kindness and support.",
    "Determined to break free from limiting beliefs and patterns.",
    "Finding purpose in the pursuit of personal growth.",
    "Advocate for authenticity and vulnerability in relationships.",
    "Inspired by the resilience of the human spirit.",
    "Striving for balance and fulfillment in all areas of life.",
    "Embracing the journey of self-discovery with gratitude and humility.",
    "Championing self-compassion as a catalyst for growth and healing.",
    "Seeking wisdom from the wisdom of the ages and the experiences of others.",
    "Dedicated to personal development and lifelong learning.",
    "On a quest for deeper meaning and fulfillment.",
    "Committed to living with intention and purpose.",
    "Seeking connection and community on the path to self-realization.",
    "Embracing the power of vulnerability and authenticity.",
    "Believer in the inherent worth and dignity of every individual.",
    "Passionate about creating positive change through personal growth.",
    "Inspired by the potential for transformation within ourselves and our communities.",
    "Striving for excellence and growth in all aspects of life.",
    "Embracing the challenges of growth with resilience and determination.",
    "Advocate for self-awareness and mindful living.",
    "Dedicated to cultivating empathy and understanding in myself and others.",
    "Seeking inspiration from the wisdom of diverse cultures and traditions.",
    "On a journey of self-discovery and self-empowerment.",
    "Committed to personal growth as a lifelong pursuit.",
    "Seeking wisdom from the collective experiences of humanity.",
    "Embracing the journey of self-mastery with courage and humility.",
    "Championing self-love and self-acceptance as the foundation for growth.",
    "Advocate for compassion and kindness in all interactions.",
    "Inspired by the resilience and strength of the human spirit.",
    "Striving for balance and harmony in mind, body, and soul.",
    "Embracing the process of self-discovery with open-heartedness.",
    "Believer in the power of community and collaboration for personal growth.",
    "Passionate about fostering empathy and understanding in the world.",
    "Inspired by the potential for positive change within ourselves and our communities.",
    "Striving for excellence and growth in every aspect of life.",
    "Embracing the challenges of personal growth with resilience and determination.",
    "Advocate for self-awareness and mindful living.",
    "Dedicated to cultivating empathy and compassion in myself and others.",
    "Seeking inspiration from the wisdom of diverse cultures and traditions.",
    "On a journey of self-discovery and self-empowerment.",
    "Committed to personal growth as a lifelong journey.",
    "Seeking wisdom from the collective experiences of humanity.",
    "Embracing the journey of self-mastery with courage and humility.",
    "Championing self-love and self-acceptance as the foundation for growth.",
    "Advocate for compassion and kindness in all interactions.",
    "Inspired by the resilience and strength of the human spirit.",
    "Striving for balance and harmony in mind, body, and soul.",
    "Embracing the process of self-discovery with open-heartedness.",
    "Believer in the power of community and collaboration for personal growth.",
    "Passionate about fostering empathy and understanding in the world.",
    "Seeking inspiration from the collective wisdom of humanity.",
    "Embracing the journey of self-discovery with an open mind and heart.",
    "Advocate for authenticity and vulnerability as pathways to growth.",
    "Dedicated to continuous self-improvement and learning.",
    "Striving to live with intention and purpose in all endeavors.",
    "On a quest for deeper understanding and connection.",
    "Committed to cultivating resilience and perseverance in the face of challenges.",
    "Seeking guidance and inspiration from fellow seekers on the path.",
    "Embracing the journey of personal growth with courage and curiosity.",
    "Believer in the transformative power of self-reflection and introspection.",
    "Passionate about creating a life of meaning and purpose.",
    "Inspired by the potential for growth and transformation within each of us.",
    "Striving for authenticity and alignment with my true self.",
    "Embracing the journey of self-discovery with humility and gratitude.",
    "Advocate for kindness, compassion, and empathy in all interactions.",
    "Dedicated to personal development and inner exploration.",
    "Seeking wisdom from the teachings of ancient and modern sages.",
    "On a journey of self-discovery and self-actualization.",
    "Committed to growth, learning, and self-improvement.",
    "Seeking connection and community on the path to self-realization.",
    "Embracing vulnerability as a strength and a catalyst for growth.",
    "Believer in the power of intention and conscious living.",
    "Passionate about fostering a culture of empathy and understanding.",
    "Inspired by the resilience and potential of the human spirit.",
    "Striving for balance and harmony in all aspects of life.",
    "Embracing the journey of self-discovery with an open heart and mind.",
    "Advocate for self-expression and authenticity in all endeavors.",
    "Dedicated to personal growth and the pursuit of excellence.",
    "Seeking inspiration from the wisdom of diverse cultures and traditions.",
    "On a quest for deeper meaning and fulfillment in life.",
    "Committed to living with intention and purpose.",
    "Seeking connection and community on the path to self-realization.",
    "Embracing the power of vulnerability and authenticity.",
    "Believer in the transformative power of self-awareness and self-reflection.",
    "Passionate about personal growth and development.",
    "Inspired by the potential for positive change within ourselves and our communities.",
    "Striving for balance and growth in mind, body, and spirit.",
    "Embracing the challenges of growth with courage and resilience.",
    "Advocate for mindfulness and self-awareness in daily life.",
    "Dedicated to cultivating empathy and compassion for all beings.",
    "Seeking wisdom from the collective experiences of humanity.",
    "On a journey of self-discovery and self-empowerment.",
    "Committed to personal growth as a lifelong journey.",
    "Seeking inspiration from the wisdom of diverse cultures and traditions.",
    "Embracing the journey of self-mastery with courage and humility.",
    "Championing self-love and self-acceptance as the foundation for growth.",
    "Advocate for compassion and kindness in all interactions.",
    "Inspired by the resilience and strength of the human spirit.",
    "Striving for balance and harmony in mind, body, and soul.",
    "Embracing the process of self-discovery with open-heartedness.",
    "Believer in the power of community and collaboration for personal growth.",
    "Passionate about fostering empathy and understanding in the world.",
    "Seeking inspiration from the collective wisdom of humanity.",
    "Enthusiastic learner embracing the journey of personal growth.",
    "Striving for authenticity and vulnerability in every interaction.",
    "Believer in the power of self-awareness and reflection for growth.",
    "Passionate about building meaningful connections and relationships.",
    "On a quest for inner peace and fulfillment.",
    "Committed to overcoming challenges and obstacles with resilience.",
    "Seeking inspiration from the wisdom of nature and the universe.",
    "Embracing the power of gratitude and positivity.",
    "Advocate for self-compassion and self-care as essential practices.",
    "Dedicated to spreading kindness and positivity wherever I go.",
    "Seeking to unleash my full potential and live my best life.",
    "Inspired by the courage and strength of those who persevere.",
    "Striving to create a life filled with purpose and passion.",
    "Embracing change as an opportunity for growth and transformation.",
    "Believer in the importance of mindfulness and presence.",
    "Passionate about personal development and continuous learning.",
    "On a journey of self-discovery and self-actualization.",
    "Committed to living authentically and aligning with my values.",
    "Seeking wisdom from the experiences of others and ancient teachings.",
    "Embracing the beauty of impermanence and the flow of life.",
    "Advocate for self-expression and creative exploration.",
    "Dedicated to fostering a culture of inclusivity and belonging.",
    "Seeking to inspire and uplift others on their journey.",
    "Embracing the unknown with curiosity and wonder.",
    "Believer in the interconnectedness of all beings.",
    "Passionate about leaving a positive impact on the world.",
    "Striving for balance and harmony in mind, body, and soul.",
    "Embracing vulnerability as a strength and source of connection.",
    "Advocate for authenticity and genuine human connection.",
    "Dedicated to cultivating resilience and inner strength.",
    "Seeking guidance from the wisdom of my intuition.",
    "On a quest for deeper meaning and spiritual growth.",
    "Committed to expanding my comfort zone and trying new things.",
    "Seeking to live with intention and purpose in all aspects of life.",
    "Embracing the journey of self-discovery with humility and grace.",
    "Believer in the power of love to heal and transform.",
    "Passionate about personal growth as a lifelong pursuit.",
    "Striving to cultivate a sense of wonder and awe in everyday life.",
    "Embracing challenges as opportunities for growth and learning.",
    "Advocate for self-reflection and introspection as tools for growth.",
    "Dedicated to being the change I wish to see in the world.",
    "Seeking inspiration from the beauty of the natural world.",
    "On a journey of self-acceptance and self-love.",
    "Committed to living authentically and embracing my uniqueness.",
    "Seeking to connect with others on a deeper level.",
    "Embracing the present moment with gratitude and mindfulness.",
    "Believer in the power of community to support and uplift.",
    "Passionate about creating a life that feels meaningful and fulfilling.",
    "Striving to live in alignment with my values and principles.",
    "Embracing the journey of personal growth with courage and curiosity.",
    "Advocate for self-care and compassion in all aspects of life.",
    "Dedicated to spreading joy and positivity wherever I go.",
    "Seeking to cultivate inner peace and tranquility.",
    "On a quest for greater self-awareness and understanding.",
    "Committed to challenging myself and pushing beyond my limits.",
    "Seeking wisdom from the depths of my own heart and soul.",
    "Embracing the beauty of imperfection and embracing my flaws.",
    "Believer in the power of gratitude to transform one's life.",
    "Passionate about personal development and self-improvement.",
    "Striving to cultivate a mindset of abundance and possibility.",
    "Embracing uncertainty as an opportunity for growth and exploration.",
    "Advocate for authenticity and vulnerability in all relationships.",
    "Dedicated to creating a life that reflects my deepest values.",
    "Seeking inspiration from the wisdom of the natural world.",
    "On a journey of self-discovery and self-empowerment.",
    "Committed to living with courage and integrity.",
    "Seeking to cultivate greater compassion and empathy for all beings.",
    "Embracing the journey of personal growth with open arms.",
    "Believer in the power of resilience and perseverance.",
    "Passionate about leaving a positive impact on the world.",
    "Striving to live a life of purpose and meaning.",
    "Embracing the journey of self-discovery with humility and grace.",
    "Advocate for self-expression and creative exploration.",
    "Dedicated to fostering a sense of connection and belonging.",
    "Seeking to inspire and uplift others on their journey.",
    "Embracing the unknown with curiosity and wonder.",
    "Believer in the power of community and collaboration.",
    "Passionate about personal growth and self-improvement.",
    "Striving to live authentically and in alignment with my values.",
    "Embracing vulnerability as a pathway to connection and growth.",
    "Advocate for mindfulness and presence in everyday life.",
    "Dedicated to cultivating resilience and inner strength.",
    "Seeking wisdom from the experiences of others and ancient teachings.",
    "On a quest for deeper meaning and spiritual growth.",
    "Committed to expanding my comfort zone and embracing new experiences.",
    "Seeking to live with intention and purpose in all aspects of life.",
    "Embracing the journey of self-discovery with courage and curiosity.",
    "Believer in the power of love to heal and transform.",
    "Passionate about personal growth as a lifelong journey.",
    "Striving to cultivate gratitude and appreciation for life's blessings.",
    "Embracing challenges as opportunities for growth and learning.",
    "Advocate for self-reflection and introspection as tools for personal growth.",
    "Dedicated to being the change I wish to see in the world.",
    "Seeking inspiration from the beauty of the natural world.",
    "On a journey of self-acceptance and self-discovery.",
    "Committed to living authentically and embracing my true self.",
    "Seeking to connect with others on a deeper level.",
    "Embracing the present moment with mindfulness and presence.",
    "Believer in the power of community to support and uplift one another.",
    "Passionate about creating a life filled with purpose and meaning.",
    "Striving to live in alignment with my values and principles.",
    "Embracing the journey of personal growth with courage and curiosity.",
    "Advocate for self-care and self-compassion in all aspects of life.",
    "Dedicated to spreading joy and positivity wherever I go.",
    "Seeking to cultivate inner peace and tranquility.",
    "On a quest for greater self-awareness and understanding.",
    "Committed to challenging myself and stepping outside of my comfort zone.",
    "Seeking wisdom from the depths of my own heart and soul.",
    "Embracing imperfection as a natural part of the human experience.",
    "Believer in the power of gratitude to transform one's perspective.",
    "Passionate about personal growth and lifelong learning.",
    "Striving to cultivate a mindset of abundance and possibility.",
    "Embracing uncertainty as an opportunity for growth and exploration.",
    "Advocate for authenticity and vulnerability in all relationships.",
    "Dedicated to creating a life that reflects my deepest values and aspirations.",
    "Seeking inspiration from the wisdom of the natural world.",
    "On a journey of self-discovery and self-empowerment.",
    "Committed to living with courage and integrity.",
    "Seeking to cultivate greater compassion and empathy for all beings.",
    "Embracing the journey of personal growth with open arms and an open heart.",
    "Believer in the power of resilience and perseverance.",
    "Passionate about leaving a positive impact on the world.",
    "Striving to live a life of purpose and meaning.",
    "Embracing the journey of self-discovery with humility, grace, and gratitude.",
    "Advocate for self-expression and creative exploration.",
    "Dedicated to fostering a sense of connection and belonging in myself and others.",
    "Seeking to inspire and uplift others on their journey of personal growth.",
    "Embracing the unknown with curiosity, wonder, and excitement.",
    "Believer in the power of community and collaboration to drive positive change.",
    "Passionate about personal growth and the pursuit of excellence in all endeavors.",
    "Striving to live authentically and in alignment with my deepest values.",
    "Embracing vulnerability as a pathway to connection, growth, and transformation.",
    "Advocate for mindfulness and presence as keys to living a fulfilling life.",
    "Dedicated to cultivating resilience and inner strength in the face of adversity.",
    "Seeking wisdom from the experiences of others and the teachings of ancient wisdom traditions.",
    "On a quest for deeper understanding, meaning, and fulfillment in life.",
    "Committed to stepping out of my comfort zone and embracing new challenges.",
    "Seeking to live with intention, purpose, and passion in every moment.",
    "Embracing the journey of self-discovery with courage, curiosity, and humility.",
    "Believer in the power of love, compassion, and empathy to transform lives.",
    "Passionate about personal growth as a lifelong journey of self-discovery.",
    "Striving to cultivate gratitude, joy, and appreciation for the beauty of life.",
    "Embracing challenges and obstacles as opportunities for growth, learning, and development.",
    "Advocate for self-awareness, self-compassion, and self-acceptance as essential practices.",
    "Dedicated to making a positive difference in the world and leaving a legacy of kindness and compassion.",
    "Seeking inspiration from the wonders of the natural world and the wisdom of ancient teachings.",
    "On a journey of self-acceptance, self-love, and self-empowerment.",
    "Committed to living authentically, boldly, and unapologetically.",
    "Seeking to connect with others on a deep, meaningful, and soulful level.",
    "Embracing the present moment with mindfulness, presence, and gratitude.",
    "Believer in the power of community, connection, and collaboration to create positive change.",
    "Passionate about creating a life of purpose, passion, and fulfillment.",
    "Striving to live in alignment with my values, vision, and highest potential.",
    "Embracing the journey of personal growth with an open heart, an open mind, and an open spirit.",
    "Advocate for self-care, self-compassion, and self-love as the foundation for a fulfilling life.",
    "Dedicated to spreading love, light, and positivity wherever I go.",
    "Seeking to cultivate inner peace, inner wisdom, and inner joy.",
    "On a quest for greater self-awareness, self-understanding, and self-realization.",
    "Committed to challenging myself, expanding my horizons, and evolving into the best version of myself.",
    "Seeking wisdom, guidance, and inspiration from the depths of my soul and the heights of the universe.",
    "Embracing impermanence, uncertainty, and change as natural and essential aspects of life.",
    "Believer in the power of gratitude, grace, and growth to elevate the human experience.",
    "Passionate about personal growth, transformation, and transcendence.",
    "Striving to cultivate a mindset of abundance, possibility, and empowerment.",
    "Embracing vulnerability, authenticity, and transparency in all relationships and interactions.",
    "Advocate for self-expression, self-exploration, and self-expansion as fundamental human rights.",
    "Dedicated to creating a life that is a work of art, a masterpiece of love, and a symphony of joy.",
    "Seeking inspiration from the wonders of nature, the mysteries of the cosmos, and the magic of life.",
    "On a journey of self-discovery, self-expression, and self-creation.",
    "Committed to living with passion, purpose, and presence in every moment.",
    "Seeking to connect with others in soulful, meaningful, and transformative ways.",
    "Embracing the power of love, light, and laughter to heal, uplift, and inspire.",
    "Believer in the interconnectedness of all beings, the oneness of all life, and the unity of all creation.",
    "Passionate about creating a world that works for everyone, where love reigns supreme and miracles abound.",
    "Striving to be a beacon of hope, a source of strength, and a catalyst for positive change in the world.",
    "Embracing the journey of personal growth, spiritual evolution, and conscious living.",
    "Advocate for peace, justice, and equality for all beings, everywhere, always.",
    "Dedicated to the path of the heart, the way of the soul, and the pursuit of happiness.",
    "Seeking to make a difference, to make an impact, and to make the world a better place for all.",
    "On a quest for truth, wisdom, and enlightenment in a world of illusion, confusion, and delusion.",
    "Committed to being the change I wish to see, the light I wish to shine, and the love I wish to share.",
    "Seeking inspiration, guidance, and support from the universe, the divine, and the infinite within.",
    "Embracing the beauty of the journey, the magic of the moment, and the mystery of existence.",
    "Believer in the power of intention, manifestation, and co-creation to shape our reality and our destiny.",
    "Passionate about personal transformation, planetary healing, and global awakening.",
    "Striving to live in alignment with my highest self, my deepest truth, and my true purpose.",
    "Embracing the journey of self-discovery, self-realization, and self-actualization.",
    "Advocate for self-empowerment, self-liberation, and self-mastery as the keys to freedom and fulfillment.",
    "Dedicated to living a life of love, joy, and abundance in harmony with all of creation.",
    "Seeking to embody the divine qualities of compassion, kindness, and forgiveness in every moment.",
    "On a journey of awakening, enlightenment, and liberation from the illusions of the ego-mind.",
    "Committed to expanding my consciousness, deepening my spirituality, and embodying my divinity.",
    "Seeking to transcend the limitations of the human condition and embrace the infinite potential of the soul.",
    "Embracing the path of the mystic, the sage, and the spiritual warrior in service to the highest good.",
    "Believer in the power of love to heal, transform, and unite all beings in oneness and harmony.",
    "Passionate about co-creating a world of peace, prosperity, and planetary sustainability for future generations.",
    "Striving to be a channel of divine grace, a vessel of divine love, and a beacon of divine light in the world.",
    "Embracing the journey of self-discovery, self-transformation, and self-realization as the purpose of life.",
    "Advocate for conscious living, conscious evolution, and conscious co-creation as the way forward for humanity.",
    "Dedicated to awakening the world to its true nature, its divine essence, and its infinite possibilities.",
    "Seeking to embody the highest virtues of wisdom, compassion, and enlightenment in every moment.",
    "On a quest for spiritual liberation, universal love, and cosmic consciousness in this lifetime.",
    "Committed to being a force for good, a catalyst for change, and a source of inspiration for all beings everywhere."
]

with open('emails.txt', 'r') as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()

# Strip newline characters from each line and store them in a new list
lines = [line.strip() for line in lines]
pics = os.listdir('pinterest_ideas')

for email in lines:
    try:
        print('init chrome incognito...')
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # This line enables incognito mode
        chrome_options.add_argument("--enable-chrome-browser-cloud-management")

        # Path to your ChromeDriver executable
        chromedriver_path = 'chromedriver-win64/chromedriver-win64/chromedriver.exe'

        # Initialize Chrome driver with Chrome options
        driver = webdriver.Chrome(options=chrome_options)
        bio = random.choice(user_bios)
        pic = random.choice(pics)
    except:
        print('big fail')



